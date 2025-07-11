import requests
from bs4 import BeautifulSoup
from datetime import datetime

pages = {
    "page1": "https://mly1.543412546.xyz/api/v1/client/subscribe?token=63f471030c4806a38e76467fa9fdd031",
    "page2": "https://xtls.rprx.vision/api/v1/client/subscribe?token=02034b23af5a70f14815ab3a7ea0159f",
    "page6": "https://mly1.543412546.xyz/api/v1/client/subscribe?token=63f471030c4806a38e76467fa9fdd031&target=clash"
}


for name, url in pages.items():
    print(f"正在抓取: {url}")
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0 Safari/537.36"
}
    response = requests.get(url=url, headers=headers, timeout=10, verify=False)
    if response.status_code == 200:
        with open(f"{name}.txt", "w", encoding="utf-8") as f:
            f.write(response.text)
