import click
import os
from colorama import Fore, Back, Style

@click.command()
@click.argument('filepath')
def main(filepath):
    if not os.path.isfile(filepath):
        print("file not found")
        return

    file = open(filepath)
    text = file.read()
    file.close()
    print_markdown(text)

def print_markdown(text: str):
    out = ""
    lines = text.splitlines()
    for l in lines:
        if l.startswith('**') and l.endswith('**'):
            out += Style.BRIGHT + l + "\n" + Style.RESET_ALL
        elif l.startswith('*') and l.endswith('*'):
            out += Fore.YELLOW + l + "\n" + Fore.RESET
        else:
            out += l + "\n"
    print(out)