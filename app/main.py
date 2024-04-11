import typer


app = typer.Typer()


@app.command()
def hello(name: str, lastname: str = ""):
    print(f"Hello {name} {lastname}")


@app.command()
def goodbye(name: str, formal: bool = False):
    if formal:
        print(f"Goodbye Ms. {name}. Have a good day.")
    else:
        print(f"Bye {name}!")


if __name__ == "__main__":
    app()
