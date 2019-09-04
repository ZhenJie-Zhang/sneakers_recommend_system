import requests
import json
import os
import random
from bs4 import BeautifulSoup
from time import sleep
import warnings
warnings.filterwarnings('ignore')
dn = "mizuno/"
domain = "http://products.mizuno.tw"
# url = "http://products.mizuno.tw/?p=0&order=p_d&st%5B0%5D=1"

start = 0
page = 6
for p in range(start, page+1):
    url = "http://products.mizuno.tw/?p=" + str(p) + "&order=p_d&st%5B0%5D=1"
    print("第" + str(p + 1) + "頁:", url)
    response = requests.get(url).text
    html = BeautifulSoup(response)
    content = html.find_all("div", class_="col-sm-6")

    for c in content:
        title = c.find("h3").text
        product_id = c.find("span", class_="productid").text
        price = c.find("span", class_="price").text
        picture = domain + c.find("img", class_="img-responsive")["src"]
        picture_big = domain + c.find("img", class_="img-responsive")["src"].replace("list", "zoom")
        link = domain + c.find("a")["href"]

        response = requests.get(link).text
        html = BeautifulSoup(response)
        detail = html.find_all("dl", id="product-detail")
        print(title, product_id, price, picture, picture_big, link, sep="\n", end="\n" + "="*15 + "\n")
        tips = [f["title"] for f in html.find_all("img", class_="tips")]
        print(tips)
        color_variation = [{"product_id": var["src"].split("/")[-1].lstrip("SH_").split(".")[0],
                            "picture": domain + var["src"]}
                           for var in html.find_all("img", class_="color-variation")]
        print(color_variation)
        saved = {"product_id": product_id,
                 "brand": "mizuno",
                 "title": title,
                 "price": price,
                 "picture": [picture, picture_big],
                 "link": link,
                 "tips": tips,
                 "color_variation": color_variation}

        for d in detail:
            spec = d.find_all("dd")
            size = spec[0].text
            try:
                material = str(spec[2]).replace("<br/>", "\n").strip("<dd>").strip("</dd>")

            except IndexError:
                material = None
                print("material is None")

            try:
                weight = spec[3].text

            except IndexError:
                weight = None
                print("weight is None")

            try:
                feature = str(spec[4]).replace("<br/>", "\n").strip("<dd>").strip("</dd>")

            except IndexError:
                feature = None
                print("feature is None")

            print(size, material, weight, feature, sep="\n")

            saved["size"] = size
            saved["material"] = material
            saved["weight"] = weight
            saved["feature"] = feature
        print(json.dumps(saved, indent=4))
        if not os.path.exists(dn):
            os.makedirs(dn)
        f = open(dn + product_id + ".json", "w", encoding="utf-8")
        json.dump(saved, f)
        f.close()
        print("-" * 20)
        random_time = random.randint(1, 3)
        print("防阻擋等待時間:", random_time, "sec")
        sleep(random_time)
