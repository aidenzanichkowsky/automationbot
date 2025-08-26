import requests
from bs4 import BeautifulSoup

def run():
    url = "https://www.bbc.com/news"
    print(f"Fetching headlines from {url} ...")
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")

    headlines = soup.select("h2")[:5]  # grab first 5 headlines
    print("\nTop News Headlines:")
    for i, h in enumerate(headlines, start=1):
        print(f"{i}. {h.text.strip()}")
