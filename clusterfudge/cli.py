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
            <!DOCTYPE html>
            <html class="h-full bg-gray-50 antialiased">

            <head>
                <title>Clusterfudge - Login</title>
                <meta name="robots" content="noindex,nofollow">
                <link rel="icon" type="image/x-icon" href="https://cdn.clusterfudge.com/favicon.ico">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <link rel="preconnect" href="https://fonts.googleapis.com">
                <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                <link href="https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400..800;1,400..800&display=swap"
                    rel="stylesheet">
                <link href="https://fonts.googleapis.com/css2?family=Inter:wght@100..900&display=swap" rel="stylesheet">
                <style>
                    body {
                        font-family: 'Inter', sans-serif;
                        font-weight: 400;
                    }

                    .logo {
                        font-family: 'EB Garamond', sans-serif;
                        font-weight: 200;
                    }
                    
                </style>
                <style>/* ! tailwindcss v3.4.3 | MIT License | https://tailwindcss.com */*,::after,::before{box-sizing:border-box;border-width:0;border-style:solid;border-color:#e5e7eb}::after,::before{--tw-content:''}:host,html{line-height:1.5;-webkit-text-size-adjust:100%;-moz-tab-size:4;tab-size:4;font-family:ui-sans-serif, system-ui, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";font-feature-settings:normal;font-variation-settings:normal;-webkit-tap-highlight-color:transparent}body{margin:0;line-height:inherit}hr{height:0;color:inherit;border-top-width:1px}abbr:where([title]){-webkit-text-decoration:underline dotted;text-decoration:underline dotted}h1,h2,h3,h4,h5,h6{font-size:inherit;font-weight:inherit}a{color:inherit;text-decoration:inherit}b,strong{font-weight:bolder}code,kbd,pre,samp{font-family:ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;font-feature-settings:normal;font-variation-settings:normal;font-size:1em}small{font-size:80%}sub,sup{font-size:75%;line-height:0;position:relative;vertical-align:baseline}sub{bottom:-.25em}sup{top:-.5em}table{text-indent:0;border-color:inherit;border-collapse:collapse}button,input,optgroup,select,textarea{font-family:inherit;font-feature-settings:inherit;font-variation-settings:inherit;font-size:100%;font-weight:inherit;line-height:inherit;letter-spacing:inherit;color:inherit;margin:0;padding:0}button,select{text-transform:none}button,input:where([type=button]),input:where([type=reset]),input:where([type=submit]){-webkit-appearance:button;background-color:transparent;background-image:none}:-moz-focusring{outline:auto}:-moz-ui-invalid{box-shadow:none}progress{vertical-align:baseline}::-webkit-inner-spin-button,::-webkit-outer-spin-button{height:auto}[type=search]{-webkit-appearance:textfield;outline-offset:-2px}::-webkit-search-decoration{-webkit-appearance:none}::-webkit-file-upload-button{-webkit-appearance:button;font:inherit}summary{display:list-item}blockquote,dd,dl,figure,h1,h2,h3,h4,h5,h6,hr,p,pre{margin:0}fieldset{margin:0;padding:0}legend{padding:0}menu,ol,ul{list-style:none;margin:0;padding:0}dialog{padding:0}textarea{resize:vertical}input::placeholder,textarea::placeholder{opacity:1;color:#9ca3af}[role=button],button{cursor:pointer}:disabled{cursor:default}audio,canvas,embed,iframe,img,object,svg,video{display:block;vertical-align:middle}img,video{max-width:100%;height:auto}[hidden]{display:none}*, ::before, ::after{--tw-border-spacing-x:0;--tw-border-spacing-y:0;--tw-translate-x:0;--tw-translate-y:0;--tw-rotate:0;--tw-skew-x:0;--tw-skew-y:0;--tw-scale-x:1;--tw-scale-y:1;--tw-pan-x: ;--tw-pan-y: ;--tw-pinch-zoom: ;--tw-scroll-snap-strictness:proximity;--tw-gradient-from-position: ;--tw-gradient-via-position: ;--tw-gradient-to-position: ;--tw-ordinal: ;--tw-slashed-zero: ;--tw-numeric-figure: ;--tw-numeric-spacing: ;--tw-numeric-fraction: ;--tw-ring-inset: ;--tw-ring-offset-width:0px;--tw-ring-offset-color:#fff;--tw-ring-color:rgb(59 130 246 / 0.5);--tw-ring-offset-shadow:0 0 #0000;--tw-ring-shadow:0 0 #0000;--tw-shadow:0 0 #0000;--tw-shadow-colored:0 0 #0000;--tw-blur: ;--tw-brightness: ;--tw-contrast: ;--tw-grayscale: ;--tw-hue-rotate: ;--tw-invert: ;--tw-saturate: ;--tw-sepia: ;--tw-drop-shadow: ;--tw-backdrop-blur: ;--tw-backdrop-brightness: ;--tw-backdrop-contrast: ;--tw-backdrop-grayscale: ;--tw-backdrop-hue-rotate: ;--tw-backdrop-invert: ;--tw-backdrop-opacity: ;--tw-backdrop-saturate: ;--tw-backdrop-sepia: ;--tw-contain-size: ;--tw-contain-layout: ;--tw-contain-paint: ;--tw-contain-style: }::backdrop{--tw-border-spacing-x:0;--tw-border-spacing-y:0;--tw-translate-x:0;--tw-translate-y:0;--tw-rotate:0;--tw-skew-x:0;--tw-skew-y:0;--tw-scale-x:1;--tw-scale-y:1;--tw-pan-x: ;--tw-pan-y: ;--tw-pinch-zoom: ;--tw-scroll-snap-strictness:proximity;--tw-gradient-from-position: ;--tw-gradient-via-position: ;--tw-gradient-to-position: ;--tw-ordinal: ;--tw-slashed-zero: ;--tw-numeric-figure: ;--tw-numeric-spacing: ;--tw-numeric-fraction: ;--tw-ring-inset: ;--tw-ring-offset-width:0px;--tw-ring-offset-color:#fff;--tw-ring-color:rgb(59 130 246 / 0.5);--tw-ring-offset-shadow:0 0 #0000;--tw-ring-shadow:0 0 #0000;--tw-shadow:0 0 #0000;--tw-shadow-colored:0 0 #0000;--tw-blur: ;--tw-brightness: ;--tw-contrast: ;--tw-grayscale: ;--tw-hue-rotate: ;--tw-invert: ;--tw-saturate: ;--tw-sepia: ;--tw-drop-shadow: ;--tw-backdrop-blur: ;--tw-backdrop-brightness: ;--tw-backdrop-contrast: ;--tw-backdrop-grayscale: ;--tw-backdrop-hue-rotate: ;--tw-backdrop-invert: ;--tw-backdrop-opacity: ;--tw-backdrop-saturate: ;--tw-backdrop-sepia: ;--tw-contain-size: ;--tw-contain-layout: ;--tw-contain-paint: ;--tw-contain-style: }.mx-4{margin-left:1rem;margin-right:1rem}.mt-10{margin-top:2.5rem}.mt-2{margin-top:0.5rem}.flex{display:flex}.h-full{height:100%}.min-h-full{min-height:100%}.flex-col{flex-direction:column}.items-center{align-items:center}.justify-center{justify-content:center}.gap-5{gap:1.25rem}.bg-gray-50{--tw-bg-opacity:1;background-color:rgb(249 250 251 / var(--tw-bg-opacity))}.bg-white{--tw-bg-opacity:1;background-color:rgb(255 255 255 / var(--tw-bg-opacity))}.px-6{padding-left:1.5rem;padding-right:1.5rem}.py-12{padding-top:3rem;padding-bottom:3rem}.pb-12{padding-bottom:3rem}.pl-2{padding-left:0.5rem}.pt-12{padding-top:3rem}.text-center{text-align:center}.text-2xl{font-size:1.5rem;line-height:2rem}.text-lg{font-size:1.125rem;line-height:1.75rem}.text-sm{font-size:0.875rem;line-height:1.25rem}.font-semibold{font-weight:600}.leading-6{line-height:1.5rem}.text-gray-900{--tw-text-opacity:1;color:rgb(17 24 39 / var(--tw-text-opacity))}.text-indigo-600{--tw-text-opacity:1;color:rgb(79 70 229 / var(--tw-text-opacity))}.antialiased{-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale}.shadow{--tw-shadow:0 1px 3px 0 rgb(0 0 0 / 0.1), 0 1px 2px -1px rgb(0 0 0 / 0.1);--tw-shadow-colored:0 1px 3px 0 var(--tw-shadow-color), 0 1px 2px -1px var(--tw-shadow-color);box-shadow:var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow)}.hover\:text-indigo-500:hover{--tw-text-opacity:1;color:rgb(99 102 241 / var(--tw-text-opacity))}.hover\:underline:hover{-webkit-text-decoration-line:underline;text-decoration-line:underline}@media (min-width: 640px){.sm\:mx-auto{margin-left:auto;margin-right:auto}.sm\:w-full{width:100%}.sm\:max-w-\[480px\]{max-width:480px}.sm\:max-w-md{max-width:28rem}.sm\:rounded-lg{border-radius:0.5rem}.sm\:px-12{padding-left:3rem;padding-right:3rem}.sm\:px-6{padding-left:1.5rem;padding-right:1.5rem}}@media (min-width: 1024px){.lg\:px-8{padding-left:2rem;padding-right:2rem}}</style>
            </head>

            <body class="h-full">

                <div class="flex min-h-full flex-col justify-center py-12 mx-4 sm:px-6 lg:px-8">

                    <div class="sm:mx-auto sm:w-full sm:max-w-[480px]">
                        <div class="bg-white px-6 pb-12 pt-12 shadow sm:rounded-lg sm:px-12">

                            <div class="flex items-center justify-center sm:mx-auto sm:w-full sm:max-w-md">
                                <div class="flex items-center">
                                    <img src="https://cdn.clusterfudge.com/img/logo-icon.svg" alt="Clusterfudge" width="40" height="40">
                                    <h2 class="logo flex items-center text-2xl pl-2">Clusterfudge</h2>
                                </div>
                            </div>

                            <div class="mt-10 gap-5 text-center text-gray-900">
                                <p class="text-lg font-semibold">Login successful!</p>
                                <p class="text-sm mt-2 leading-6">You can now return to your terminal. For more information about the Clusterfudge platform, please visit our <a class="font-semibold leading-6 text-indigo-600 hover:text-indigo-500 hover:underline" href="https://docs.clusterfudge.com/" target="_blank" rel="noopener noreferrer">documentation</a>.</p>
                            </div>
                        </div>


                    </div>
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
