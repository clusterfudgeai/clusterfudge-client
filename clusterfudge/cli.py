import asyncio
import contextlib
import json
import os
import shutil
import sys
import webbrowser
from pathlib import Path
from typing import Optional

import grpc
import typer
from aiohttp import web
from clusterfudge_proto.tunnelpb import tunnel_pb2
from typing_extensions import Annotated

from clusterfudge import Client

app = typer.Typer(
    name="clusterfudge",
    no_args_is_help=True,
    invoke_without_command=True,
    add_completion=False,
)


def _parse_host(host: str) -> str:
    """Hosts are of the form <exec-command-id>.ssh.clusterfudge.com"""
    split_host = host.split(".")
    if len(split_host) != 4:
        raise ValueError(
            f"Invalid host format: {host}. Expected <exec-command-id>.ssh.clusterfudge.com"
        )
    return split_host[0]


def _get_clusterfudge_path() -> str:
    """Get the path to the clusterfudge binary."""
    return shutil.which("clusterfudge") or "clusterfudge"


@app.command()
def configure_ssh(
    config_file: Path = typer.Option(
        Path.home() / ".ssh" / "config",
        help="Path to the SSH config file",
        exists=False,
        file_okay=True,
        dir_okay=False,
        writable=True,
        readable=True,
    ),
):
    """
    Configure SSH to use Clusterfudge as a ProxyCommand for *.ssh.clusterfudge.com.
    """
    clusterfudge_path = _get_clusterfudge_path()

    config_content = f"""
Host *.ssh.clusterfudge.com
    ProxyCommand {clusterfudge_path} ssh %h
"""

    if config_file.exists():
        with config_file.open("r") as f:
            existing_content = f.read()
        if "*.ssh.clusterfudge.com" in existing_content:
            typer.echo("✅ Clusterfudge SSH configuration already exists.")
            return

        config_content = f"{existing_content}\n{config_content}"

    with config_file.open("w") as f:
        f.write(config_content)

    typer.echo(f"✅ Clusterfudge SSH configuration has been added to {config_file}")
    typer.echo("You can now connect using: ssh <exec-command-id>.ssh.clusterfudge.com")


@app.command()
def ssh(
    host: str,
    verbose: bool = typer.Option(
        False, "--verbose", "-v", help="Enable verbose logging"
    ),
):
    """
    Act as an SSH ProxyCommand, tunneling SSH traffic through a gRPC stream.
    """
    exec_command_id = _parse_host(host)
    asyncio.run(_run_tunnel(exec_command_id, verbose))


async def _connect_stdin_stdout():
    loop = asyncio.get_event_loop()
    reader = asyncio.StreamReader()
    protocol = asyncio.StreamReaderProtocol(reader)
    await loop.connect_read_pipe(lambda: protocol, sys.stdin)
    w_transport, w_protocol = await loop.connect_write_pipe(
        asyncio.streams.FlowControlMixin, sys.stdout
    )
    writer = asyncio.StreamWriter(w_transport, w_protocol, reader, loop)
    return reader, writer


async def _run_tunnel(exec_command_id: str, verbose: bool):
    client = Client()
    reader, writer = await _connect_stdin_stdout()

    async def generate_requests():
        yield tunnel_pb2.TunnelRequest(
            initialise=tunnel_pb2.InitialiseRequest(exec_command_id=exec_command_id)
        )

        while True:
            try:
                data = await reader.read(4096)
                if not data:
                    break
                yield tunnel_pb2.TunnelRequest(data=tunnel_pb2.Data(data=data))
            except IOError:
                break

    if verbose:
        print(
            f"Starting SSH tunnel for {exec_command_id}.ssh.clusterfudge.com",
            file=sys.stderr,
        )

    try:
        async for response in client.tunnel_stub.Tunnel(generate_requests()):
            writer.write(response.data)
            await writer.drain()
    except grpc.RpcError as e:
        print(e, file=sys.stderr)
        raise e
    finally:
        await client.channel.close()


async def _login(tenant_id: Optional[str] = None):
    future = asyncio.Future()

    async def on_auth(request):
        print("Handling request to /auth")
        token = request.query.get("token")
        if token:
            print(f"Received token: {token}")
            future.set_result(token)
        else:
            print("No token found in request")
            future.set_result(None)

        html_content = """
            <html>
            <head>
                <style>
                    body {
                        font-family: sans-serif;
                        background-color: hsl(240 10% 3.9%);
                        text-align: center;
                        color: white;
                        font-size: 16px;
                    }
                    .logo {
                        font-family: 'Quantico', sans-serif;
                        text-shadow: 1px 1px 0px red;
                        letter-spacing: 0.05em;
                        font-style: italic;
                        font-weight: 700;
                        text-transform: uppercase;
                        font-size: 1.5rem;
                        margin: 2rem 0;
                    }
                </style>
            </head>
            <body>
                <h1 class="logo">Clusterfudge</h1>
                <div>
                    <p style="padding:3em;">Login successful, you can now return to your terminal to start using Clusterfudge.</p>
                    <p>If you have not already installed the <b>fudgelet</b> on your nodes, please follow the instructions <a href="https://docs.clusterfudge.com/quickstart#2-install-the-fudgelet-on-a-linux-node">here</a>.</p>
                    <p>More documentation about the Clusterfudge platform can be found <a href="https://docs.clusterfudge.com/">here</a>.</p>
                </div>
            </body>
            </html>
            """
        return web.Response(body=html_content, content_type="text/html")

    @contextlib.asynccontextmanager
    async def _run_local_server():
        app = web.Application()
        app.router.add_get("/auth", on_auth)
        runner = web.AppRunner(app)
        await runner.setup()
        site = web.TCPSite(runner, "localhost", 0)
        try:
            await site.start()
            yield site._server.sockets[0].getsockname()[1]
        finally:
            await site.stop()

    async with _run_local_server() as port:
        redirect_url = f"http://localhost:{port}/auth"
        auth_url = f"https://clusterfudge.clusterfudge.com/auth?clipath={redirect_url}"
        if tenant_id:
            auth_url += f"&tenantId={tenant_id}"

        typer.echo(f"Opening browser to {auth_url}")
        webbrowser.open_new(auth_url)

        await future
        typer.echo("Login successful")
        token = future.result()

    _save_token_to_file(token)
    typer.echo("")
    typer.echo(
        "If you have not already installed the fudgelet on your nodes, please follow the instructions at https://docs.clusterfudge.com/quickstart#2-install-the-fudgelet-on-a-linux-node"
    )
    typer.echo("")
    typer.echo("Otherwise, you're ready to start launching with Clusterfudge")
    typer.echo("")


def _save_token_to_file(token: str):
    token_data = {"token": token}
    config_dir = os.path.join(os.path.expanduser("~"), ".clusterfudge")
    os.makedirs(config_dir, exist_ok=True)
    filepath = os.path.join(config_dir, "config.json")
    with open(filepath, "w") as token_file:
        json.dump(token_data, token_file)
    typer.echo("Token saved to file successfully.")


@app.command()
def login(
    tenant_id: Annotated[
        Optional[str],
        typer.Argument(
            help="Override tenant ID for login.",
            hidden=True,
        ),
    ] = None
):
    asyncio.run(_login(tenant_id))


@app.callback()
def callback():
    pass


if __name__ == "__main__":
    app()
