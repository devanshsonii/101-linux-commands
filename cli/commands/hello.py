import typer

app = typer.Typer()

@app.callback(invoke_without_command=True)
def hello(name: str):
    print(f"Hello {name}")
    