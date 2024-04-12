import typer
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from rich.progress import Progress, SpinnerColumn, TextColumn
from utils import print_md

app = typer.Typer()

load_dotenv()


@app.command()
def start():
    llm = ChatOpenAI()
    result = llm.invoke("how can langsmith help with testing?")
    print(result)

    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are world class technical documentation writer. Answer with a markdown."),
        ("user", "{input}")
    ])
    output_parser = StrOutputParser()

    chain = prompt | llm | output_parser

    with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            transient=True,
    ) as progress:
        progress.add_task(description="Processing...", total=None)
        result = chain.invoke({"input": "how can langsmith help with testing?"})
    # print(result)

    print_md(result)



@ app.command()
def hello(name: str, lastname: str = ""):
    print(f"Hello {name} {lastname}")


if __name__ == "__main__":
    app()
