from urllib.request import urlretrieve

import requests
from bs4 import BeautifulSoup
import time
import random
import json
import os

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
            wd = r.find("a", class_="BaseGridItem__content___3LORP")["href"]
            time.sleep(random.randint(1, 3))

            saved = {"鞋名": title,
                    "價錢": price1,
                    "圖片網址": picture,
                    "超連結": wd}
            print(saved)
            dn = "yahoo_man/"
            # 建立資料夾並在沒有目錄時建立
            if not os.path.exists(dn):
                os.makedirs(dn)
            ## 儲存內文(JSON)
            f = open(dn + "/" + title + ".json", "w", encoding="utf-8")
            json.dump(saved, f)
            f.close()
            # 下載圖片
            # 多 import 一個 urlretrieve 的功能
            fn = dn + "/" + title + ".jpg"
            urlretrieve(picture, fn)

        except:
            try:
                title = str.strip(r.find("span", class_="BaseGridItem__title___2HWui").text)
                price2 = str.strip(r.find("em", class_="BaseGridItem__price___31jkj").text)
                picture = str.strip(str.strip(r.find("img", class_="SquareImg_img_2gAcq")["srcset"]).split(",")[1])[:-3]
                wd = r.find("a", class_="BaseGridItem__content___3LORP")["href"]
                time.sleep(random.randint(1, 3))

                saved = {"鞋名": title,
                         "價錢": price1,
                         "圖片網址": picture,
                         "超連結": wd}
                print(saved)
                dn = "yahoo_man/"
                # 建立資料夾並在沒有目錄時建立
                if not os.path.exists(dn):
                    os.makedirs(dn)
                ## 儲存內文(JSON)
                f = open(dn + "/" + title + ".json", "w", encoding="utf-8")
                json.dump(saved, f)
                f.close()
                # 下載圖片
                # 多 import 一個 urlretrieve 的功能
                fn = dn + "/" + title + ".jpg"
                urlretrieve(picture, fn)
            except:
                print("這雙跳過")
    page = page + 1