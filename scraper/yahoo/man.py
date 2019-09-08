import requests
from bs4 import BeautifulSoup
import time
import random
import os
import json


page = 1
while True:
    url = "https://tw.buy.yahoo.com/category/31407672?pg=" + str(page)
    response = requests.get(url)

    html = BeautifulSoup(response.text, 'html.parser')
    rs = html.find_all("li", class_="BaseGridItem__grid___2wuJ7 imprsn BaseGridItem__multipleImage___37M7b")

    for r in rs:
        try:
            title = str.strip(r.find("span", class_="BaseGridItem__title___2HWui").text)
            price1 = str.strip(r.find("span", class_="BaseGridItem__price___31jkj").text)
            picture = str.strip(str.strip(r.find("img", class_="SquareImg_img_2gAcq")["srcset"]).split(",")[1])[:-3]
            # print("鞋名: ", title.text)
            # print("特價/原價: ", price1.text)
            # print("圖片網址: ", picture["srcset"])

            time.sleep(random.randint(1, 3))

            saved = {"鞋名": title,
                    "特價/原價": price1,
                    "圖片網址": picture}
            print(json.dumps(saved, indent=4))
        except:
            title = str.strip(r.find("span", class_="BaseGridItem__title___2HWui").text)
            price2 = str.strip(r.find("em", class_="BaseGridItem__price___31jkj").text)
            picture = str.strip(str.strip(r.find("img", class_="SquareImg_img_2gAcq")["srcset"]).split(",")[1])[:-3]
            # print("價錢: ", price2.text)
            # print("圖片網址: ", picture["srcset"])
            time.sleep(random.randint(1, 3))

            saved = {"鞋名": title,
                    "價錢": price2,
                    "圖片網址": picture}
            print(json.dumps(saved, indent=4))
    page = page + 1