import typer
from commands.hello import app as hello_app

app = typer.Typer()
app.add_typer(hello_app, name="hello")

if __name__ == "__main__":
    app()
