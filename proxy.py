import requests
from rich.console import Console
from rich.table import Table
from rich.progress import track
import socket

console = Console()

PROXY_URLS = {
    "socks5": [
        "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt",
        "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all"
    ],
    "socks4": [
        "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks4.txt",
        "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=10000&country=all&ssl=all&anonymity=all"
    ]
}

def fetch_proxies(proxy_type):
    proxies = []
    for url in PROXY_URLS[proxy_type]:
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            proxies.extend(response.text.strip().split("\n"))
        except requests.RequestException:
            console.print(f"Failed to fetch proxies from [red]{url}[/red]")
    return proxies

def test_proxy(proxy, proxy_type, timeout):
    ip, port = proxy.split(":")
    try:
        if proxy_type == "socks5":
            s = socket.create_connection((ip, int(port)), timeout=timeout)
            s.close()
            return True
        elif proxy_type == "socks4":
            s = socket.create_connection((ip, int(port)), timeout=timeout)
            s.close()
            return True
    except:
        return False

def main():
    console.print("[bold blue]ZEX Proxy List[/bold blue]", justify="center")
    console.print("Choose proxy type:\n[1] socks5\n[2] socks4\n\n", justify="left")
    choice = console.input("Enter your choice: ")

    if choice == "1":
        proxy_type = "socks5"
    elif choice == "2":
        proxy_type = "socks4"
    else:
        console.print("[red]Invalid choice![/red]")
        return

    proxies = fetch_proxies(proxy_type)
    console.print(f"Fetched [green]{len(proxies)} {proxy_type}[/green] proxies.")

    save_without_test = console.input("Do you want to save proxies without testing? (y/n): ")
    if save_without_test.lower() == 'y':
        with open(f"{proxy_type}_zex.txt", "w") as f:
            f.write("\n".join(proxies))
        console.print(f"Saved [green]{len(proxies)} {proxy_type}[/green] proxies to [green]{proxy_type}_zex.txt[/green].")
        return

    timeout = float(console.input("Enter timeout for testing (default is 1): ") or 1)
    working_proxies = []
    for proxy in track(proxies, description=f"Testing {proxy_type} proxies..."):
        if test_proxy(proxy, proxy_type, timeout):
            working_proxies.append(proxy)

    with open(f"{proxy_type}_zex.txt", "w") as f:
        f.write("\n".join(working_proxies))

    console.print(f"Saved [green]{len(working_proxies)} {proxy_type}[/green] proxies to [green]{proxy_type}_zex.txt[/green].")

if __name__ == "__main__":
    main()
