import requests
import os
import pandas as pd
from bs4 import BeautifulSoup
from time import sleep
from warnings import filterwarnings
filterwarnings("ignore")

def get_page_meta(url):
    response = requests.get(url, headers=headers)
    html = BeautifulSoup(response.text)

    product = html.find_all("div", id="ppd")
    result = {}
    for p in product:
        title = p.find("h1", id="title").text.strip()
        brand_link = domain + p.find("a", id="brand")["href"]
        brand_pic = p.find("img", id="brand")["src"]
        star = p.find("span", id="acrPopover")["title"].replace(" 顆星，最高 5 顆星", "")
        price = p.find("span", id="priceblock_ourprice").text.split(" - ")
        color = ",".join([i["alt"] for i in p.find_all("img", class_="imgSwatch")])
        comment = p.find("span", id="acrCustomerReviewText").text

        print(title, brand_link, brand_pic)
        print(star, price[0], price[1], color)
        print(comment)
        result["title"] = title
        result["brand_link"] = brand_link
        result["brand_pic"] = brand_pic
        result["star"] = star
        result["price_low"] = price[0]
        result["price_high"] = price[1]
        result["color"] = color
        result["comment"] = comment

    feature = html.find("div", id="productDescription")\
                  .find_all("p")

    feature_cn = feature[0].text.strip()
    feature_en = feature[1].text.strip()
    print(feature_cn)
    print(feature_en)
    result["feature_cn"] = feature_cn
    result["feature_en"] = feature_en

    feature_detail = html.find("div", id="detailBullets_feature_div").find_all("li")
    asin = feature_detail[2].find_all("span")[-1].text
    print(asin)
    result["asin"] = asin

    return result



domain = "https://www.amazon.com"

headers = {
    "accept-language": "zh-TW,zh;q=0.9,ja-JP;q=0.8,ja;q=0.7,en-US;q=0.6,en;q=0.5",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/76.0.3809.132 Safari/537.36 "
}
# 服裝，鞋子和珠寶 : 男士時裝 : 鞋 : 運動 : 慢跑 : 路跑

url = "https://www.amazon.com/Skechers-AFTER-BURN-M-FIT-Memory-Lace-Up-Sneaker/dp/B00D881KE6/ref=lp_14210389011_1_1?s=apparel&ie=UTF8&qid=1568777254&sr=1-1&nodeID=14210389011&psd=1"

dn = "./amazon1/"

page = 1
count = 0
download = 0

file_list = os.listdir(dn)

while True:
    url = "https://www.amazon.com/s?" \
          "i=fashion-mens-intl-ship&" \
          "bbn=16225019011&" \
          "rh=n%3A16225019011%2Cn%3A679255011%2Cn%3A6127770011%2Cn%3A679286011&dc&" \
          "page=" + str(page) + "&" \
          "pf_rd_i=16225019011&" \
          "pf_rd_m=ATVPDKIKX0DER&" \
          "pf_rd_p=23429fae-990f-41b5-b328-862bb645dd6a&" \
          "pf_rd_r=1DZK4TJYM27GRZNZSF72&" \
          "pf_rd_s=merchandised-search-2&" \
          "pf_rd_t=101&qid=1567740449&" \
          "rnid=6127770011&" \
          "ref=sr_pg_" + str(page)

    response = requests.get(url, headers=headers).text
    html = BeautifulSoup(response, 'lxml')
    print(html.find_all("img"))

    product = html.find_all('div', class_='s-include-content-margin')
    print(product)
    picture = [[pic.split(' ')[0]
                for pic in str(pics.find('img', class_='s-image')['srcset']).split(', ')]
               for pics in product]
    if len(picture) == 0:
        print("本次爬取概要")
        print("共", page - 1, "頁", "共", count, "筆", "\n共下載:", download, "筆")
        break

    else:
        count += len(picture)
        print("第", page, "頁，共", len(picture), "筆")

        for i, p in enumerate(picture):
            fn = p[0].split('/')[-1].split('.')
            try:
                fn.pop(1)
                fn = '.'.join(fn)

            except IndexError:
                pass

            finally:
                print(i, p[0], fn, end=' ')

                try:
                    response = requests.get(p[0], stream=True)

                except IndexError:
                    print("不能下載")
                    break

                if not os.path.exists(dn):
                    os.makedirs(dn)

                elif fn not in file_list:
                    print("正在下載", end=" ")
                    file_list.append(fn)
                    f = open(dn + fn, "wb")
                    f.write(response.raw.read())
                    f.close()
                    time = random.randint(1, 3)
                    print("等待時間", time)
                    download += 1
                    sleep(time)

                else:
                    print("下載過了")
    print("=" * 50)
    page += 1