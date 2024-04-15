import typer
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()

app = typer.Typer()


@app.command()
def basic():
    llm = ChatOpenAI(model="gpt-3.5-turbo")
    prompt = """You are a travel agent that helps with people's trips on a budget. 
    
Question: What would be a good itinerary for spending three days in Romania and 3 days in Israel?

Answer: """

    result = llm.invoke(prompt)
    print(result.context)


@app.command()
def template():
    llm = ChatOpenAI(model="gpt-4-turbo")

    template = """You are a travel agent that helps with people's trips about {interest} on a budget of {budget}. 
    
Question: What would be a good itinerary for spending three days in Romania and 3 days in Israel?

Answer: """

    prompt_template = PromptTemplate(
        input_variables=["interest", "budget"],
        template=template
    )
    prompt = prompt_template.format(interest="fishing", budget="5000 USD")
    result = llm.invoke(prompt)
    print(result.content)


if __name__ == "__main__":
    app()
