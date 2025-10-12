import requests
### 爬蟲get的練習
### 把爬蟲程序偽裝為正常瀏覽器
# head = {"User-Agent": "Mozilla/5.0(Windows NT 10.0; Win64; x64)"}
# response = requests.get("http://books.toscrape.com/")
# if response.ok:
#     print(response.text)
# else:
#     print("請求失敗")

### 爬蟲練習
from bs4 import BeautifulSoup
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"
}

for start_num in range(0, 250, 25):
    response = requests.get(f"http://movie.douban.com/top250?start={start_num}", headers=headers)
# print(response.text)
# 檢查反回的數字是否成功
# print(response.status_code)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    all_titles = soup.find_all("span", attrs={"class": "title"})
    for title in all_titles:
        if '/' not in title.string:
            print(title.string)
