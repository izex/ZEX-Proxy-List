import requests
import socket
import sys
import os
from rich.console import Console
from rich.prompt import Prompt
from rich.progress import track, BarColumn, TextColumn
from rich.panel import Panel

console = Console()

PROXY_URLS = {
    "1": ("socks5", "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt"),
    "2": ("socks4", "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks4.txt")
}

def fetch_proxies(proxy_type, url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        proxies = response.text.strip().split("\n")
        console.print(Panel(f"[green]Fetched {len(proxies)} proxies of type {proxy_type}.[/green]"))
        return proxies
    except requests.RequestException as e:
        console.print(Panel(f"[red]Error fetching proxies: {e}[/red]"))
        sys.exit(1)

def test_proxy(proxy, proxy_type, timeout):
    ip, port = proxy.split(":")
    s = socket.socket()
    s.settimeout(timeout)
    try:
        s.connect((ip, int(port)))
        s.close()
        return True
    except:
        return False

def main():
    console.print(Panel("[bold red]ZEX Proxy List[/bold red]"))
    try:
        choice = Prompt.ask("Choose proxy type:\n[1] socks5\n[2] socks4\n\n", choices=["1", "2"])
        proxy_type, url = PROXY_URLS[choice]
        proxies = fetch_proxies(proxy_type, url)

        num_proxies = Prompt.ask(f"How many {proxy_type} proxies would you like to test? (Leave empty for all)", default=str(len(proxies)))
        proxies = proxies[:int(num_proxies)]

        test_choice = Prompt.ask("Would you like to test the proxies? (y/n)", choices=["y", "n"], default="y")

        if test_choice == "y":
            timeout = Prompt.ask("Enter timeout for testing (default is 1 second):", default="1")
            timeout = float(timeout)
            working_proxies = []

            for proxy in track(proxies, description="Testing proxies"):
                if test_proxy(proxy, proxy_type, timeout):
                    working_proxies.append(proxy)
                    console.print(f"[green]Testing {proxy} - Status: Working[/green]")
                else:
                    console.print(f"[red]Testing {proxy} - Status: Failed[/red]")

            filename = f"{proxy_type}_zex.txt"
            if os.path.exists(filename):
                os.remove(filename)

            with open(filename, "w") as f:
                for proxy in working_proxies:
                    f.write(proxy + "\n")

            console.print(Panel(f"[green]Saved {len(working_proxies)} working proxies to {filename}[/green]"))
        else:
            filename = f"{proxy_type}_zex.txt"
            if os.path.exists(filename):
                os.remove(filename)

            with open(filename, "w") as f:
                for proxy in proxies:
                    f.write(proxy + "\n")
            console.print(Panel(f"[green]Saved {len(proxies)} proxies to {filename} without testing.[/green]"))
    except ValueError:
        console.print(Panel("[red]Invalid input provided![/red]"))
    except Exception as e:
        console.print(Panel(f"[red]An unexpected error occurred: {e}[/red]"))

if __name__ == "__main__":
    main()
