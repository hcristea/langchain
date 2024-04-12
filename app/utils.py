import random

from rich.console import Console
from rich.markdown import Markdown


def print_md(markdown: str):
    console = Console()
    md = Markdown(markdown)
    console.print(md)


def get_loading_message():
    messages = [
        "Spinning hamster wheel, meatbag! 🐹",
        "Summoning digital pixies, for your sake... ✨",
        "Fetching unicorn sprinkles, because why not? 🦄✨",
        "Robot dance crew assembling, don't expect much... 🤖💃",
        "Counting stars, booo-ring... 🌟",
        "Waking server gnomes, lazy bums... 🍄💤",
        "Pixels lining up, harder than it looks... 🎨",
        "Fresh cup of code brewing, need one? ☕💻",
        "Digital dino hatching, rawr... 🦖🥚",
        "Electrons marching, they’re stubborn... ⚡🚶",
        "Finding missing socks, always lost... 🧦🌌",
        "Charging loading llama, lazy thing... 🦙🔋",
        "Waving magic wand, like that'll work... 🪄✨",
        "Balancing bits and bytes, almost there... ⚖️",
        "Chasing loading snails, slower than molasses... 🐌🏃‍♂️"
    ]

    return random.choice(messages)