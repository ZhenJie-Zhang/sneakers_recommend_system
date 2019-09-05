import requests
import time
from bs4 import BeautifulSoup
import random
import json
import warnings
warnings.filterwarnings("ignore")
import os


width = 540
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
}

for page in range(1, 78):

    print("page= ", page)
    url = "https://feature.com/collections/footwear?page=" + str(page) + "&view=ajax"
    response = requests.get(url, headers=headers)
    html = BeautifulSoup(response.text)
    pictures = html.find_all("div", class_="collection-products-carousel")
    pic = pictures[0].find_all("img", class_="img-fluid")
    time.sleep(random.randint(1, 2))

    for image in range(12):
        try:
            print("image= ", image)
            url_contain = 'https://feature.com' + pictures[image].find('a')['href']
            response_contain = requests.get(url_contain, headers=headers)
            html_contain = BeautifulSoup(response_contain.text)
            contain = html_contain.find("div", id="Productivo")
            name = str.strip(contain.find('h1').text)

            # =============找內文=======================
            discribe = contain.find('section', id="content1")
            discribe1 = discribe.find('p')
            discribe2 = discribe.find("ul")
            discribe3 = discribe2.find_all('li')
            li_dis = ''
            for dis_li in discribe3:
                li_dis += str.strip(dis_li.text) + " "
            text = str.strip(discribe1.text) + str.strip(li_dis)
            # =========================================

            # ==============找價格======================
            price = contain.find('span', id="ProductPrice")
            price = str.strip(price.text)
            # =========================================

            pic = pictures[image].find_all("img", class_="img-fluid")
            picture_list = []

            # ==========抓4張圖片=======================
            for pic_4 in pic:
                picture_list.append("https:" + str(pic_4["data-src"]).replace("{width}", str(width)))
            # print("picture= ", picture_list)
            # =========================================
            time.sleep(random.randint(1, 2))


        except:
            print("第" + str(page) + "頁到底囉!")

        saved = {
            "title": name,
            "price": price,
            "picture": picture_list,
            "text": text
        }
        dn = "feature_pictures/"
        if not os.path.exists(dn):
            os.makedirs(dn)
        # print(json.dumps(saved, indent=4))
        fn = str.lower(name.replace(" ", "_").replace("/", "_").replace("\"", "").replace("\'", "").replace("_-_", "-")) + ".json"

        f = open(dn + fn, "w", encoding="utf-8")
        json.dump(saved, f)
        f.close()