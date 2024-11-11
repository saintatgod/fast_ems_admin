from fastapi import FastAPI
import uvicorn
import typer
from app.core.config import settings
from app.core.init_app import lifespan

def create_app() -> FastAPI:
    app = FastAPI(**settings.get_backend_attributes, lifespan=lifespan)
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
