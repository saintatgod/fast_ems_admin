from fastapi import FastAPI
import uvicorn
import typer
from starlette.staticfiles import StaticFiles

from app.core.config import settings
from app.core.init_app import lifespan, reset_api_docs
from app.api import ApiRouter

def create_app() -> FastAPI:
    app = FastAPI(**settings.get_backend_attributes, lifespan=lifespan)

    if settings.STATIC_ENABLE:
        app.mount(settings.STATIC_URL, StaticFiles(directory=settings.STATIC_ROOT), name=settings.STATIC_URL)

    app.include_router(ApiRouter, prefix=settings.API_PREFIX)

    reset_api_docs()

    return app

app_shell = typer.Typer()

@app_shell.command()
def run():
    uvicorn.run(
        app='main:create_app',  # 确保 main.py 是文件名
        host=settings.SERVER_HOST,
        port=settings.SERVER_PORT,
        lifespan="on",
        factory=True
    )

@app_shell.command()
def hello():
    typer.echo("Hello, World!")

if __name__ == '__main__':
    app_shell()
