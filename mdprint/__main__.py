import click
import os
import re
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
        elif l.startswith('`') and l.endswith('`'):
            out += Fore.CYAN + l + "\n" + Fore.RESET
        elif '[' in l and ']' in l and '(' in l and ')' in l:
            l = l.replace('[', '')
            l = l.replace(']', '')
            l = l.replace('(', '(' + Fore.BLUE)
            l = l.replace(')', Fore.RESET + ')')
            out += l
        elif re.match(r"\d\.", l) != None:
            l = re.split(r'(\s+)', l)
            l.insert(0, Fore.GREEN)
            l.insert(2, Fore.RESET)
            l = "".join(l)
            out += l + "\n"
        else:
            out += l + "\n"
    print(out)