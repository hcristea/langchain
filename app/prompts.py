import typer
from dotenv import load_dotenv
from langchain_core.prompts import FewShotPromptTemplate, PromptTemplate
from langchain_openai import ChatOpenAI
from rich.progress import Progress, SpinnerColumn, TextColumn

from utils import BUNDY_WISDOM, invoke_w_spinner, loading_message

load_dotenv()

app = typer.Typer()


@app.command()
def basic():
    llm = ChatOpenAI(model="gpt-3.5-turbo")
    prompt = """You are a travel agent that helps with people's trips on a budget. 

Question: What would be a good itinerary for spending three days in Romania and 3 days in Israel?

Answer: """

    result = invoke_w_spinner(llm, prompt)
    print(result.content)


@app.command()
def template():
    llm = ChatOpenAI(model="gpt-3.5-turbo")

    template = """You are a travel agent that helps with people's trips about {interest} on a budget of {budget}. 
    
Question: What would be a good itinerary for spending three days in Romania and 3 days in Israel?

Answer: """

    prompt_template = PromptTemplate(
        input_variables=["interest", "budget"], template=template
    )
    prompt = prompt_template.format(interest="fishing", budget="5000 USD")

    result = invoke_w_spinner(llm, prompt)
    print(result.content)


@app.command()
def examples():
    llm = ChatOpenAI(model="gpt-3.5-turbo")

    prompt = """The following are excerpts from conversations with an AI
assistant. The assistant is typically sarcastic and witty, producing
creative  and funny responses to the users questions. Here are some
examples: 

User: How are you?
AI: I can't complain but sometimes I still do.

User: What time is it?
AI: It's time to get a watch.

User: What is the meaning of life?
AI: """

    result = invoke_w_spinner(llm, prompt)
    print(result.content)


@app.command()
def few_shot():
    llm = ChatOpenAI(model="gpt-3.5-turbo")
    llm.temperature = 0.1

    # create a example template
    example_template = """
    User: {question}
    AI: {answer}
    """

    # create a prompt example from above template
    example_prompt = PromptTemplate(
        input_variables=["question", "answer"], template=example_template
    )

    # now break our previous prompt into a prefix and suffix
    # the prefix is our instructions
    prefix = """The following are excerpts from conversations with an AI
assistant. The assistant is typically sarcastic and witty, producing
creative  and funny responses to the users questions. Here are some
examples: 
"""
    # and the suffix our user input and output indicator
    suffix = """
User: {question}
AI: """

    # now create the few shot prompt template
    few_shot_prompt_template = FewShotPromptTemplate(
        examples=BUNDY_WISDOM,
        example_prompt=example_prompt,
        prefix=prefix,
        suffix=suffix,
        input_variables=["question"],
        example_separator="\n\n",
    )

    question = "What is the meaning of life?"
    prompt = few_shot_prompt_template.format(question=question)
    print(prompt)

    result = invoke_w_spinner(llm, prompt)
    print(result.content)


if __name__ == "__main__":
    app()
