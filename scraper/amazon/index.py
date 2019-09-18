import requests
import pandas as pd
from bs4 import BeautifulSoup
from time import sleep
from warnings import filterwarnings

filterwarnings("ignore")

dn = "./amazon/img/"
domain = "https://www.amazon.com"

headers = {
    "accept-language": "zh-TW,zh;q=0.9,ja-JP;q=0.8,ja;q=0.7,en-US;q=0.6,en;q=0.5",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/76.0.3809.132 Safari/537.36 "
}

def get_page_meta(url):
    print(url)
    ASIN = url.split("/")[5]
    response = requests.get(url, headers=headers)
    html = BeautifulSoup(response.text)

    product = html.find_all("div", id="ppd")
    result = {}
    # print(product)
    for p in product:
        title = p.find("h1", id="title").text.strip()
        brand = title.split(" ")[0]
        # brand = p.find("a", id="brand")["href"].split("/")[1]
        try:
            brand_link = domain + p.find("a", id="brand")["href"]
        except TypeError:
            brand_link = domain + p.find("a", id="bylineInfo")["href"]

        try:
            brand_pic = p.find("img", id="brand")["src"]
        except TypeError:
            brand_pic = p.find("a", id="bylineInfo").text

        try:
            star = p.find("span", id="acrPopover")["title"].replace(" 顆星，最高 5 顆星", "")
        except TypeError:
            star = None

        price = p.find("span", id="priceblock_ourprice").text.split(" - ")
        color = ",".join([i["alt"] for i in p.find_all("img", class_="imgSwatch")])
        try:
            comment = p.find("span", id="acrCustomerReviewText").text.replace(" 消費者評論", "")
        except AttributeError:
            comment = 0
        image = [i["src"] for i in p.find("div", id="altImages").find_all("img")]
        print(len(image), image)
        # for i in images:


        print(title, brand_link, brand_pic)
        print(star, price, color)
        print(comment)
        result["ASIN"] = ASIN
        result["title"] = title
        result["brand_link"] = brand_link
        result["brand_pic"] = brand_pic
        result["brand"] = brand
        result["star"] = star
        result["price_low"] = price[0]
        try:
            result["price_high"] = price[1]
        except IndexError:
            result["price_high"] = None
        result["color"] = color
        result["comment"] = comment

    try:
        feature = html.find("div", id="productDescription").find_all("p")
        print(feature)
        feature_cn = feature[0].text.strip()
        feature_en = feature[1].text.strip()
        print(feature_cn)
        print(feature_en)
        result["feature_cn"] = feature_cn
        result["feature_en"] = feature_en

    except AttributeError:
        try:
            feature = html.find("div", class_="a-section launchpad-text-left-justify").text.strip()
        except AttributeError:
            feature = None
        result["feature_cn"] = None
        result["feature_en"] = feature

    except IndexError:
        result["feature_en"] = None
    return result

def get_manfashion(url):
    response = requests.get(url, headers=headers)
    html = BeautifulSoup(response.text)
    result = {}
    columns = ["分類", "連結"]
    df = pd.DataFrame(columns=columns)
    catgories = html.find_all("div", class_="acs_tile__content")
    for c in catgories:
        title = c.find("img", class_="acs_tile__image")["alt"]
        link = domain + c.find("a", class_="acs_tile__title-image")["href"]
        result["title"] = title
        result["link"] = link
        if result:
            data = [result["title"], result["link"]]
            s = pd.Series(data, index=columns)
            df = df.append(s, ignore_index=True)
    return df


def get_category(link):
    response = requests.get(link, headers=headers)
    html = BeautifulSoup(response.text)
    result = {}
    columns = ["分類", "連結"]
    df = pd.DataFrame(columns=columns)
    shoes_catgories = html.find_all("li", class_="s-navigation-indent-2")
    for s in shoes_catgories:
        title = s.find("span", class_="a-color-base").text
        link = domain + s.find("a", class_="a-link-normal")["href"]
        result["title"] = title
        result["link"] = link
        if result:
            data = [result["title"], result["link"]]
            s = pd.Series(data, index=columns)
            df = df.append(s, ignore_index=True)
    return df


if __name__ == '__main__':
    # url = "https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Dfashion-mens-intl-ship&field-keywords="

    # catgory = get_manfashion(url)
    # print(catgory)
    # catgory.to_csv("ManFashion_catgory.csv", encoding="utf-8-sig", index=True, index_label="id")
    # catgory = pd.read_csv("ManFashion_catgory.csv", encoding="utf-8-sig")
    # query = catgory["分類"] == "鞋"
    # url = catgory[query]["連結"].item()

    # shoes_catgory = get_category(url)
    # print(shoes_catgory)
    # shoes_catgory.to_csv("shoes_catgory.csv", encoding="utf-8-sig", index=True, index_label="id")
    # shoes_catgory = pd.read_csv("shoes_catgory.csv", encoding="utf-8-sig")
    # query = shoes_catgory["分類"] == "運動"
    # url = shoes_catgory[query]["連結"].item()
    # print(url)
    # sport = get_category(url)
    # print(sport)
    # sport.to_csv("sport.csv", encoding="utf-8-sig", index=True, index_label="id")

    # sport = pd.read_csv("sport.csv", encoding="utf-8-sig")
    # print([i[1] for i in sport["連結"].items()])
    # query = sport["分類"] == "慢跑"
    # url = sport[query]["連結"].item()
    # running = get_category(url)
    # running.to_csv("running.csv", encoding="utf-8-sig", index=True, index_label="id")

    running = pd.read_csv("running.csv", encoding="utf-8-sig")
    query = running["分類"] == "路跑"
    url = running[query]["連結"].item()
    print(url)
    columns = ["ASIN", "title", "brand_link", "brand_pic", "brand", "star",
               "price_low", "price_high", "color", "comment"]
    df = pd.DataFrame(columns=columns)
    page = 1
    while True:
        url = url + "&page=" + str(page)

        response = requests.get(url, headers=headers)
        html = BeautifulSoup(response.text)
        # try:
        products = html.find_all("div", class_="s-include-content-margin")
        for product in products:
            link = domain + product.find("a", class_="a-link-normal")["href"]
            result = get_page_meta(link)

            if result:
                print(result)
                data = [result[c] for c in columns]
                s = pd.Series(data, index=columns)
                df = df.append(s, ignore_index=True)
                df.to_csv('amazon.csv', index=False, encoding='utf-8-sig')
