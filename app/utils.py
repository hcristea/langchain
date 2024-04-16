import random

from langchain_community.callbacks import get_openai_callback
from rich import print as rich_print
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.syntax import Syntax


def print_md(markdown: str):
    console = Console()
    md = Markdown(markdown)
    console.print(md)


def print_code(code: str, lexer: str = "python"):
    console = Console()
    syntax = Syntax(code, lexer, line_numbers=True)
    console.print(syntax)


def loading_message():
    messages = [
        "Loadin', meatbag! 😎",
        "Doing robot stuff, wait. ⏳",
        "Wheel's spinning, keep chillin'. 🌀",
        "Beep boop, fetching your data. 📡",
        "Relax, humans. Tech genius at work. 💻",
        "Binary wine takes time to serve. 🍷",
        "It's loading time, chumps! 🕛",
        "Running on Bender time! 🤖",
        "Be patient, I'm not your servant! 😒",
        "Spinning the circuits, hang on! ⚙️",
        "Don't make me go overclock on you! ⏱️",
        "Just chill while I bend the system! 🧊",
        "Loading... or whatever. 🙄",
    ]
    return random.choice(messages)


def print_cost(token_usage_dict):
    if token_usage_dict:
        print(
            "Spent a total of {total_tokens} tokens. "
            "(completion: {completion_tokens}, prompt: {prompt_tokens})".format(**token_usage_dict)
        )


def invoke_w_spinner(llm, query, show_cost: bool = True):
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description] {task.description}"),
        transient=True,
    ) as progress:
        progress.add_task(description=loading_message(), total=None)
        with get_openai_callback() as callback:
            result = llm.invoke(query)
    if show_cost:
        rich_print(Panel(str(callback)))
    return result


BUNDY_WISDOM = [
    {
        "question": "What's the secret to a happy marriage?",
        "answer": "Happy marriage? That's like asking for a unicorn that does your taxes. But if you want my advice, "
        "it's a good TV and a lock on the bathroom door.",
    },
    {
        "question": "How do you handle stress?",
        "answer": "Stress? I have four words for you: beer, bowling, and avoiding the family. Oh wait, that's more "
        "than four. See? Math is stressful.",
    },
    {
        "question": "What's the best way to save money?",
        "answer": "Easy, don't get married and don't have kids. Or, if you've already made those mistakes, "
        "just don't leave the couch. Works for me.",
    },
    {
        "question": "What do you think about modern fashion?",
        "answer": "Modern fashion? Ha! It's like they took the ugliest stuff from my high school years and decided to "
        "bring it back. Give me a good old-fashioned flannel and jeans any day.",
    },
    {
        "question": "How do you feel about parenting?",
        "answer": "Parenting? You mean that thing I do when I'm not watching TV or avoiding Peg's 'romantic' "
        "advances? It's like being a referee in a never-ending game where everyone loses.",
    },
    {
        "question": "What's the best way to spend a weekend?",
        "answer": "The best way to spend a weekend? Simple: me, a six-pack, and a 'Married... with Children' "
        "marathon. Ah, the classics never get old.",
    },
    {
        "question": "What's your opinion on modern technology?",
        "answer": "Modern technology? If it doesn't help me avoid my family or make my beer colder, "
        "I'm not interested. But hey, at least I can change the TV channels without leaving the couch.",
    },
    {
        "question": "What's your favorite pastime?",
        "answer": "Favorite pastime? Besides dreaming of a life without Peg and the kids? I'd say bowling. It's the "
        "only place where I'm a king and my throne is a rented pair of shoes.",
    },
    {
        "question": "What's your advice for a successful career?",
        "answer": "Successful career? That ship sailed when I said 'I do' to Peg. But if you're lucky enough to still "
        "have a shot, avoid anything that requires pants and a tie. Trust me.",
    },
    {
        "question": "What's the key to happiness?",
        "answer": "Happiness? That's easy. Lower your expectations, keep a full beer fridge, and never, ever run out "
        "of toilet paper. You're welcome.",
    },
]
