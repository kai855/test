import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = "https://baidu.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0 Safari/537.36"
}
response = requests.get(url, headers=headers, timeout=10)
soup = BeautifulSoup(response.text, "html.parser")
title = soup.title.string if soup.title else "No Title"

filename = f"content-{datetime.now().strftime('%Y-%m-%d')}.txt"

with open(filename, "w", encoding="utf-8") as f:
    f.write(f"Title: {title}\n")
    f.write("Page content:\n")
    f.write(response.text[:2000])  # 只取前2000字符做示例

print(f"已保存为 {filename}")
