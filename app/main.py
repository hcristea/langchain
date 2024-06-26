import typer
import chains
import prompts

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from rich.progress import Progress, SpinnerColumn, TextColumn
from utils import invoke_w_spinner, loading_message

load_dotenv()

app = typer.Typer()
app.add_typer(chains.app, name="chains")
app.add_typer(prompts.app, name="prompts")


@app.command()
def quickstart():
    llm = ChatOpenAI(model="gpt-3.5-turbo")
    # result = llm.invoke("What is git and what can you do with it?")
    # print(result)
    # return

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are GitHub power user. Answer my question like I'm 5."),
            # ("system", "You are GitHub power user. Answer my question like I'm an 90 years old grandma."),
            ("user", "{question}"),
        ]
    )
    output_parser = StrOutputParser()

    chain = prompt | llm | output_parser

    result = invoke_w_spinner(
        chain,
        {"question": "What are git hub actions and what can you do with it?"},
        show_cost=False,
    )
    print(result)


if __name__ == "__main__":
    app()
