import ipapi
from rich.console import Console
from rich.table import Table
from colorama import Fore, Style
from rgbprint import Color, gradient_print

console = Console()
C1 = Color.blue
C2 = Color.cyan

IP_BANNER = """
  ___ ___   _______ ___  ____  __
 |_ _| _ \\ |_  / __| _ \\/  \\ \\/ /
  | ||  _/  / /| _||   / () >  < 
 |___|_|   /___|___|_|_\\__/_/\\_\\
"""

def clear():
    print("\033c", end="")

def show_banner():
    gradient_print(IP_BANNER, start_color=C1, end_color=C2)
    print(Fore.BLUE + "┌───────────────────────────┐" + Style.RESET_ALL)
    print(Fore.BLUE + "│ TikTok : @zer0x_cybersecurity │" + Style.RESET_ALL)
    print(Fore.BLUE + "│ X      : @zer0x_cybersec        │" + Style.RESET_ALL)
    print(Fore.BLUE + "└───────────────────────────┘\n" + Style.RESET_ALL)

def ip_lookup(ip):
    clear()
    show_banner()
    data = ipapi.location(ip)

    table = Table(title=f"IP Information - {ip}", style="cyan")
    table.add_column("Field", style="blue")
    table.add_column("Value", style="magenta")

    output = []
    for k, v in data.items():
        table.add_row(k, str(v))
        output.append(f"{k} : {v}")

    console.print(table)

    save = input(Fore.BLUE + "Do you want to create a file with IP info? [y/n]: " + Style.RESET_ALL).lower()
    if save == "y":
        filename = f"{ip}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"IP Information - {ip}\n\n")
            for line in output:
                f.write(line + "\n")
        print(Fore.BLUE + f"\nSaved successfully: {filename}" + Style.RESET_ALL)

def main():
    cont = ""
    while cont != "n":
        ip = input(Fore.BLUE + "Enter target IP: " + Style.RESET_ALL)
        ip_lookup(ip)
        cont = input(Fore.BLUE + "\nDo you want to continue? [y/n]: " + Style.RESET_ALL).lower()
        clear()
    main()
