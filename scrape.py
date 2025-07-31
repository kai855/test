import requests
from bs4 import BeautifulSoup
from datetime import datetime


pages1 = {
    "page1": "",
    "page11": "https://ml11.hfhfb.homes/api/v1/client/subscribe?token=1023232a61975e5745e60aaaae61e0ca",
    "page2": " https://fsc.wangpankehuduan.homes/answer/land?token=aca6749abfc0ee0cd4bdf23e1a04c338",
    "page22": " https://xtls.rprx.vision/api/v1/client/subscribe?token=a49c8d24c16f8295952c716fdbaa4280",
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
