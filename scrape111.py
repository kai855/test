import requests
from bs4 import BeautifulSoup
from datetime import datetime

pages = {
    "page1": "https://mly1.543412546.xyz/api/v1/client/subscribe?token=63f471030c4806a38e76467fa9fdd031",
    "page2": "https://xtls.rprx.vision/api/v1/client/subscribe?token=02034b23af5a70f14815ab3a7ea0159f",
    "page6": "https://xtls.rprx.vision/api/v1/client/subscribe?token=7b41daca53605b52db95c01d97fd77e5"
}


for name, url in pages.items():
    print(f"正在抓取: {url}")
    headers = {
    "User-Agent": "Clash/1.9.0 (+https://github.com/Dreamacro/clash )"
}
    response = requests.get(url=url, headers=headers, timeout=10, verify=False)
    if response.status_code == 200:
        with open(f"{name}.txt", "w", encoding="utf-8") as f:
            f.write(response.text)
