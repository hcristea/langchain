import inspect

import typer
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.llm import LLMChain
from langchain.chains.llm_math.base import LLMMathChain
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_openai import ChatOpenAI, OpenAI

from utils import invoke_w_spinner, print_code

app = typer.Typer()


@app.command()
def math(show_prompt: bool = False, show_call: bool = False):
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
def docs():
    llm = ChatOpenAI(model="gpt-3.5-turbo")
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "Answer the question based on the context below:\n\n{context}"),
            ("user", "{question}")
        ],
    )

    chain = create_stuff_documents_chain(llm, prompt)

    docs = [
        Document(page_content="Veronica loves Paylocity but hates Trinet"),
        Document(page_content="George loves Dayforce but not as much as he loves PlanSource"),
        Document(page_content="Steve loves Paylocity and in a love/hate relationship with Xero"),
        Document(page_content="Everybody hate ADP"),
    ]

    query = {
        "context": docs,
        # "question": "What is everyone's favourite vendor?",
        "question": "Which vendor George hates more?",
    }
    result = invoke_w_spinner(chain, query)
    print(result)


if __name__ == "__main__":
    app()
