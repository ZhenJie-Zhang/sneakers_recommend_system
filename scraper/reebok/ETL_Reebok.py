import requests
import json
import os
from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
import warnings
warnings.filterwarnings('ignore')
page = 0

domain = "https://www.reebok.com"

headers = {
        "accept-language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7"
    }

while True:
    url = "https://www.reebok.com/us/men-shoes?start=" + str(page*48)
    # url = "https://www.reebok.com/us/men-shoes?start=48"
    # page  = page + 48
    print("目前圖片累積數:",page*48)
    try:
        response = requests.get(url).text

    except:
        break

    html = BeautifulSoup(response)
    contexts = html.find_all("div", class_="gl-product-card-container")
    # print(context)
    for context in contexts:
        picture = context.find("img", class_="gl-product-card__image")["src"]
        name = context.find("div", class_="gl-product-card__name gl-label gl-label--m").text
        # price = html.find("div", class_="gl-product-card__details-main")
        link = domain + context.find("a")["href"]
        product_id = link.split("/")[-1].split(".")[0]
        category = context.find("div", class_="gl-product-card__category")["title"]
        # print(category)
        # print(picture, name, link, sep="\n")
        # print(product_id)

        # respone = requests.get(link, headers=headers).text
        # html = BeautifulSoup(response)
        # description = html.find_all("div", class_="row")
        # print(description)

        url = "https://www.reebok.com/api/search/product/" + product_id + "?sitePath=us"

        # print(url)
        response = requests.get(url, headers=headers).text
        product = json.loads(response)
        # print(json.dumps(product, indent=4))

        # print(product["price"])


        saved = {"category": category,
                 "picture": picture,
                 "title": name,
                 "link": link,
                 "product_id": product_id,
                 "price": product["price"],
                 "color": product["color"],
                 "brand": "Reebok"
        }

        dn = "Reebok/"
        fn = dn + product_id + ".json"
        if not os.path.exists(dn):
            os.makedirs(dn)
        f = open(fn, "w", encoding="utf-8")
        json.dump(saved, f)
        f.close()

        dn = "Reebok/"
        fn = dn + picture.split("/")[-1]
        if not os.path.exists(dn):
            os.makedirs(dn)
        try:
            urlretrieve(picture, fn)

        except :
            print("不能下載")

        if len(picture) == 0:
           print("沒有了")
           break
        # for p in picture:
        #     print(p)
        # for q in name:
        #     print(q)
        # for r in price:
        #     print(r)
    page = page + 1
