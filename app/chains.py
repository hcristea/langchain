import typer


app = typer.Typer()


@app.command()
def hello():
    print("Hello Chains!")


if __name__ == "__main__":
    app()
