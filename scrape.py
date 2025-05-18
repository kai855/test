import requests
from bs4 import BeautifulSoup
from datetime import datetime

pages = {
    "page1": "https://mly1.543412546.xyz/api/v1/client/subscribe?token=615c69d35a156a4e94b0c5f9e77c811d ",
    "page2": "https://xtls.rprx.vision/api/v1/client/subscribe?token=02034b23af5a70f14815ab3a7ea0159f"
}


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0 Safari/537.36"
}
response = requests.get(url, headers=headers, timeout=10, verify=False)
soup = BeautifulSoup(response.text, "html.parser")
title = soup.title.string if soup.title else "No Title"

filename = f"content-{datetime.now().strftime('%Y-%m-%d')}.txt"

with open(filename, "w", encoding="utf-8") as f:
    f.write(f"Title: {title}\n")
    f.write("Page content:\n")
    f.write(response.text)  


for name, url in pages.items():
    print(f"正在抓取: {url}")
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0 Safari/537.36"
}
    response = requests.get(url=url, headers=headers, timeout=10, verify=False)
    if response.status_code == 200:
        with open(f"{name}.txt", "w", encoding="utf-8") as f:
            f.write(response.text)
