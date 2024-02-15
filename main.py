### simple proxy gen with proxyscrape api ###

import requests, os, time
from colorama import *
def gp(pc):
        url = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all"
        response = requests.get(url)
        proxies = response.text.split("\r\n")
        return proxies[:pc]


def banner():
    os.system("cls")
    print(Fore.CYAN + """ 
███████╗ ██████╗ ██████╗ 
╚════██║██╔═████╗╚════██╗
    ██╔╝██║██╔██║ █████╔╝
   ██╔╝ ████╔╝██║ ╚═══██╗
   ██║  ╚██████╔╝██████╔╝
   ╚═╝   ╚═════╝ ╚═════╝ 
""")

def main():
    banner()
    print("\n\n\n\nhow many proxies would you like to generate?\n\n\n\n\n\n\n")
    a = input("> ")
    proxies = gp(int(a))
    with open('proxies.txt', 'w') as f:
        for proxy in proxies:
             f.write(proxy + "\n")
    print(f"{a} proxies have been saved to proxies.txt")
    time.sleep(3)
    main()

main()
