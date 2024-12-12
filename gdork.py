import requests
from bs4 import BeautifulSoup
import urllib.parse
import time

class GoogleDorkScanner:
    def __init__(self, output_file="dork_results.txt"):

        self.base_url = "https://www.google.com/search"
        self.output_file = output_file

    def search_dork(self, dork_query, num_results=10):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        params = {
            "q": dork_query,
            "num": num_results
        }

        # Encode URL parameters
        encoded_query = urllib.parse.urlencode(params)
        search_url = f"{self.base_url}?{encoded_query}"

        response = requests.get(search_url, headers=headers)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            links = []
            for item in soup.select(".tF2Cxc a"):
                link = item["href"]
                links.append(link)
            return links
        else:
            return f"Error: {response.status_code} - {response.reason}"

    def save_results(self, results):
    
        with open(self.output_file, "a") as file:
            for link in results:
                file.write(f"{link}\n")

if __name__ == "__main__":
    # ANSI color code for green
    GREEN = "\033[92m"
    RESET = "\033[0m"

    # ASCII Banner with Creator Info in Green
    banner = f"""
{GREEN}
██████╗     ██████╗  ██████╗ ██████╗ ██╗  ██╗
██╔════╝     ██╔══██╗██╔═══██╗██╔══██╗██║ ██╔╝
██║  ███╗    ██║  ██║██║   ██║██████╔╝█████╔╝ 
██║   ██║    ██║  ██║██║   ██║██╔══██╗██╔═██╗ 
╚██████╔╝    ██████╔╝╚██████╔╝██║  ██║██║  ██╗
 ╚═════╝     ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝
              Created by: Aung San Oo
             Website: https://aungsanoo.com
{RESET}
"""
    print(banner)

    # Interactive prompts
    print("[+] Welcome to the Google Dork Scanner!")
    dork_query = input("[+] Enter the Dork Search Query: ").strip()
    num_results = input("[+] Enter the Number of Websites to Display: ").strip()
    
    # Validate input
    try:
        num_results = int(num_results)
        if num_results <= 0:
            raise ValueError
    except ValueError:
        print("[-] Invalid number of results. Please enter a positive integer.")
        exit()

    # Create scanner instance
    scanner = GoogleDorkScanner()

    print(f"\n[+] Searching for: {dork_query}")
    results = scanner.search_dork(dork_query, num_results=num_results)
    
    if isinstance(results, list):
        print("\n[+] Results:")
        for link in results:
            print(link)
    else:
        print(results)

    # Save results to file
    scanner.save_results(results)
    print(f"\n[+] Results have been saved to {scanner.output_file}.")
