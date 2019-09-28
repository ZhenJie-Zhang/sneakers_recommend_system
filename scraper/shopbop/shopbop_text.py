from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
import os
import json
# import requests
# import pandas as pd
import time
import random
# from lxml import etree

dict_nm_wb = []
item = 43#item=536 19/09/21 2213+Item=968 19/09/22 0936+Item=2324 19/09/22 1050+Item=962 19/09/22 1050
while True:
    try:
        url0 = "https://www.shopbop.com/shoes/br/v=1/13438.htm?baseIndex=" + str(item) + "00"
        response = urlopen(url0)
        html0 = BeautifulSoup(response)

        for item0 in range(0, 100):
            shoes_web = html0.find("ul", class_="products flex-flow-inline").find_all("a", class_="photo")[item0]["href"]
            print(shoes_web)
            dict_nm_wb.append(shoes_web)
            print(dict_nm_wb)
            print("*" * 20)
        print("Page", item + 1)
        time.sleep(random.randint(1, 2))
        print("-" * 20)
        item0 = 0
        item += 1
    except IndexError:
        item_n = 1
        number = len(dict_nm_wb)
        for i in range(0, number + 1):
            # 抓取單個鞋資料
            url0 = "https://www.shopbop.com/" + dict_nm_wb[i]
            response = urlopen(url0)
            html0 = BeautifulSoup(response)

            shoes_data = html0.find("div", class_="page-detail")
            # print(shoes_data )
            try:
                category = shoes_data.find("div", class_="enlarged-product-title").text.replace("/", "").replace('"', " ").replace('*', " ")
            except:
                category = "null"
            name = shoes_data.find("span", class_="brand-name").text
            price = shoes_data.find("span", class_="pdp-price").text
            color = shoes_data.find("span", class_="selectedColorLabel").text
            sizes = [s.text.replace("\n                    ", "") for s in shoes_data.find_all("div", class_="sizeBox")]
            print(sizes)

            try:
                details = [s.text.strip(" ") for s in shoes_data.find("ul", class_="bulleted-attributes").find_all("li")]
            except:
                details = "null"
            print(details)

            try:
                style = shoes_data.find("div", class_="product-code").find("span").text
            except:
                style = "null"
            try:
                about = shoes_data.find("div", class_="designerBioSectionContent").text.replace("\n", "").replace("\t","").strip("        ")
            except:
                about = "null"
            picture = shoes_data.find("img", class_="display-image")["src"]

            print('category:', category)
            print('name:', name)
            print('price:', price)
            print('color:', color)
            print('sizes:', sizes)  #
            print('details:', details)  #
            print('style:', style)
            print('about:', about)
            print('picture:', picture)
            print("-" * 20)
            data = {
                "category": category,
                "name": name,
                "price": price,
                "color": color,
                "sizes": sizes,
                "details": details,
                "style": style,
                "about": about,
                "picture": picture,
                "web": url0
            }

            print(data)
            notallowed = ["/", "|", "\\", "?",
                          "\"", "*", ":", "<",
                          ">", ".", "！", " "]
            name_revised = ""
            for c in name:
                if not c in notallowed:
                    name_revised = name_revised + c
            dn = "shopbop/"
            # 建立資料夾並在沒有目錄時建立
            if not os.path.exists(dn):
                os.makedirs(dn)
            ## 儲存內文(JSON)
            f = open(dn + category + "_" + name + ".json", "w", encoding="utf-8")
            json.dump(data, f)
            f.close()

            time.sleep(1)

            # 下載圖片
            # 多 import 一個 urlretrieve 的功能
            fn = dn + category + "_" + name + "." + picture.split(".")[-1]
            urlretrieve(picture, fn)
            print("Item ", item_n)
            item_n += 1

            print("+" * 20)
        break