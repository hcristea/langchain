import inspect

import typer
from langchain.chains.llm import LLMChain
from langchain.chains.llm_math.base import LLMMathChain
from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAI

from utils import invoke_w_spinner, print_code

app = typer.Typer()


@app.command()
def utility(show_prompt: bool = False, show_call: bool = False):
    llm = OpenAI()
    chain = LLMMathChain.from_llm(llm, verbose=True)

    # we set the prompt to only have the question we ask
    # prompt = PromptTemplate(input_variables=['question'], template='{question}')
    # chain = LLMChain(prompt=prompt, llm=llm, verbose=True)

    result = invoke_w_spinner(chain, "What is 13 raised to the .3432 power?")
    print(result)

    if show_prompt:
        print(chain.prompt.template)

    if show_call:
        print_code(inspect.getsource(chain._call))
        print_code(inspect.getsource(chain._process_llm_result))


@app.command()
def generic():
    pass


if __name__ == "__main__":
    app()
