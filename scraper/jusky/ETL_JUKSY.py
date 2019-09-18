import requests
from bs4 import BeautifulSoup
import warnings
import pandas as pd
from time import gmtime, strftime
warnings.filterwarnings('ignore')

headers = {
        "accept-language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7"
    }
page = 86248
start = 0

columns = ["日期", "標題", "內容", "網址"]
df = pd.DataFrame(columns=columns)

while page <= 94422:
    url = "https://www.juksy.com/archives/" + str(page) + "?channel=45"
    print(strftime("%Y-%m-%d %H:%M:%S", gmtime()), url, end=" ")
    response = requests.get(url).text
    html = BeautifulSoup(response)
    try:
        date = html.find("span", class_="gtm_article_title_info").text[:10]
        title = html.find("h1", class_="article__title gtm_article_title_name").text
        article = html.find("section", class_="mainArticle").text
        article_string = str(article)

        if "鞋" in article_string:
            start = start + 1
            s = pd.Series([date, title, article, url], index=columns)
            df = df.append(s, ignore_index=True)
            print(start, page, "新增寫入")
            # 輸出CSV
            df.to_csv("JUKSY2.csv", encoding="utf-8-sig", index=False)

        else:
            print(start, page, "這篇文章，沒有「鞋」")

    except AttributeError:
        print(start, page, "404 not found，這篇文章，沒有內容")

    page = page + 1
