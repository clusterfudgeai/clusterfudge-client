import asyncio
import contextlib
import json
import os
import webbrowser
from typing import Optional

import typer
from aiohttp import web
from typing_extensions import Annotated

app = typer.Typer(
    name="clusterfudge",
    no_args_is_help=True,
    invoke_without_command=True,
    add_completion=False,
)


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
        return web.Response(body=html_content, content_type='text/html')

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
    typer.echo("If you have not already installed the fudgelet on your nodes, please follow the instructions at https://docs.clusterfudge.com/quickstart#2-install-the-fudgelet-on-a-linux-node")
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
