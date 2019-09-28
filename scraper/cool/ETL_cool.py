import requests
from bs4 import BeautifulSoup
import warnings
import pandas as pd
import time
warnings.filterwarnings('ignore')
headers = {
        "accept-language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7"
    }
#起始頁數
page = 1

#計數起始數
start = 0

#寫入CSV格式
columns = ["日期", "標題", "內容", "網址"]
df = pd.DataFrame(columns=columns)

#1~151頁前為2019年的文章
while page <= 151:

    #第1層頁面的網址,1頁包含10篇文章
    url = ("https://www.cool-style.com.tw/wd2/archives/category/sneaker%E7%90%83%E9%9E%8B/page/"+ str(page))
    #讀取每頁10篇文章的頁面
    response = requests.get(url).text
    #每讀取1頁休眠3秒
    time.sleep(3)
    html = BeautifulSoup(response)

    #如發生錯誤的處理
    try:
        #取出頁面中各篇文章的網址
        artical_url = html.find_all("div", class_="read-more")
        for r in artical_url:
            #萃取出連結網址
            url = r.find("a")["href"]
            print(url, end=" ")
            #讀取各篇文章內容的頁面
            response = requests.get(url).text
            #每讀取1頁休眠1秒
            time.sleep(1)
            html = BeautifulSoup(response)
            #取出文章內容
            article = html.find("div", class_="article-content").text

            #取出標題
            title = html.find("h3", class_="post-title").text

            #取出日期
            date = html.find("div", class_="date").text

            #寫入計數依次+1
            start = start + 1

            #寫入CSV格式
            s = pd.Series([date, title, article, url], index=columns)
            df = df.append(s, ignore_index=True)
            print("第",page,"頁","第",start,"篇", "新增寫入")
            # 輸出CSV
            df.to_csv("cool2019_v1.1.csv", encoding="utf-8-sig", index=False)


    #錯誤處理
    except AttributeError:
        print("寫入第",start,"篇時發生錯誤,略過")

    #頁面計數依次+1
    page = page + 1

