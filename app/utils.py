import random

from rich.console import Console
from rich.markdown import Markdown


def print_md(markdown: str):
    console = Console()
    md = Markdown(markdown)
    console.print(md)


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
