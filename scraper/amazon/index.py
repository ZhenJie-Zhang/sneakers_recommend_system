import requests
import pandas as pd
import os
import random
from bs4 import BeautifulSoup
from time import sleep
from datetime import datetime
from warnings import filterwarnings

filterwarnings("ignore")

dn = "./amazon/img/"
fn = datetime.now().strftime("amazon-%Y%m%d%H%M.csv")
domain = "https://www.amazon.com"
user_agents = [
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.8 (KHTML, like Gecko) Beamrise/17.2.0.9 Chrome/17.0.939.0 Safari/535.8',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7',
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5',
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; SV1; .NET CLR 1.1.4322)',
        'Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50',
        'Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50',
        'Opera/9.80(Macintosh;IntelMacOSX10.6.8;U;en)Presto/2.8.131Version/11.11',
        'Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11']

headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "accept-encoding": "gzip, deflate, br",
            "cache-control": "max-age=0",
            "accept-language": "zh-TW,zh;q=0.9,ja-JP;q=0.8,ja;q=0.7,en-US;q=0.6,en;q=0.5",
            "user-agent": random.choice(user_agents),
            "cookie": """aws-priv=eyJ2IjoxLCJldSI6MCwic3QiOjB9; aws-target-static-id=1560494069657-81731; aws-target-data=%7B%22support%22%3A%221%22%7D; s_fid=23702F43EBBB5D20-0568221326992E2C; session-id=145-6873007-2152334; session-id-time=2082787201l; sp-cdn="L5Z9:TW"; ubid-main=131-8626244-2372658; x-wl-uid=18jEl9ECOsUrDVk3Au9lytr0gRo2T27A1zaI43UJo4xDbaeja4TedUg9OVvxGMrLIVt4UFmN9IAg=; skin=noskin; aws_lang=tw; s_cc=true; aws-target-visitor-id=1560494069660-96739.22_33; aws-mkto-trk=id%3A112-TZM-766%26token%3A_mch-aws.amazon.com-1568612464248-31828; aws-ubid-main=910-8675238-8373003; aws-business-metrics-last-visit=1568612619561; aws-account-alias=cxcxc-learning; aws-userInfo=%7B%22arn%22%3A%22arn%3Aaws%3Aiam%3A%3A129729052534%3Auser%2Fstudent19%22%2C%22alias%22%3A%22cxcxc-learning%22%2C%22username%22%3A%22student19%22%2C%22keybase%22%3A%22l%2B3axisItfjK5KoE1zY0kfUaAUU42loMUG%2F%2FPRyWKLU%5Cu003d%22%2C%22issuer%22%3A%22http%3A%2F%2Fsignin.aws.amazon.com%2Fsignin%22%7D; regStatus=registered; aws-session-id=482-0013835-5519685; c_m=undefinedwww.google.comSearch%20Engine; s_sq=%5B%5BB%5D%5D; noflush_locale=en; s_vn=1592030069812%26vn%3D4; s_dslv=1568615377984; s_nr=1568615377990-Repeat; aws-session-id-time=1568621919l; lc-main=zh_TW; i18n-prefs=TWD; session-token=V1OtkN/lZo1tDjbRUsNKRmNmD4FoZ4StvupIm3gVcww54wxbT+MsZ6CM0w+Qo4DgK2e+HPBB/DPp5Wzh+Q49GzwIhKEbQXCCShskGs0/pNHZQuj4YJ9jO6RSxiXzKFmvrDSD5qZzWeLTDc1yZZ+rbjy2QgwV74HrzwviSHqO6mI9qk/mJBZH75rYreDYNYtv; x-amz-captcha-1=1568885604466499; x-amz-captcha-2=gXy3HuIcVzQJ6S2HnrGFqg==; csm-hit=tb:s-30PR2YTHRVKTCFMQTQR1|1568878744035&t:1568878744634&adb:adblk_no""",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "same-origin",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1"
        }

def get_page_meta(url):
    ASIN = url.split("/")[5]
    wait = random.randint(3, 5)
    sleep(wait)
    response = requests.get(url, headers=headers)
    html = BeautifulSoup(response.text)

    product = html.find_all("div", id="ppd")
    result = {}
    for i, p in enumerate(product):
        title = p.find("h1", id="title").text.strip()
        brand = title.split(" ")[0]
        images = [i["src"] for i in p.find("div", id="altImages").find_all("img")]
        feature_ls = p.find_all("ul", class_="a-unordered-list a-vertical a-spacing-none")
        feature = "".join([f.text.strip() for f in feature_ls])
        try:
            price = p.find("span", id="priceblock_ourprice").text.split(" - ")
        except AttributeError:
            price = None
            print('result["price"] = None')

        try:
            color = ",".join([i["alt"] for i in p.find_all("img", class_="imgSwatch")])
            color_pic = ",".join([i["src"] for i in p.find_all("img", class_="imgSwatch")])
        except AttributeError:
            color = None
            print('result["color"] = None')
            color_pic = None
            print('result["color_pic"] = None')

        try:
            star = p.find("span", id="acrPopover")["title"].replace(" 顆星，最高 5 顆星", "")
        except TypeError:
            star = None
            print('result["star"] = None')

        try:
            price_low = price[0]
        except TypeError:
            price_low = None
            print('result["price_low"] = None')


        try:
            price_high = price[1]
        except IndexError:
            price_high = None
            print('result["price_high"] = None')
        except TypeError:
            price_high = None
            print('result["price_high"] = None')

        try:
            comment = p.find("span", id="acrCustomerReviewText").text.replace(" 消費者評論", "")
        except AttributeError:
            comment = None
            print('result["comment"] = None')

        finally:
            result["ASIN"] = ASIN
            result["brand"] = brand
            result["url"] = url
            result["images"] = ",".join(images)
            result["title"] = title
            result["star"] = star
            result["color"] = color
            result["color_pic"] = color_pic
            result["comment"] = comment
            result["price_low"] = price_low
            result["price_high"] = price_high
            result["feature"] = feature
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
    columns = ["ASIN", "images", "title", "brand_link", "brand_pic", "brand", "star",
               "price_low", "price_high", "color", "color_pic", "comment", "feature_cn", "feature_en"]
    # df = pd.DataFrame(columns=columns)
    page = 1
    count = 0
    while True:
        headers["user-agent"] = random.choice(user_agents)
        url = url + "&page=" + str(page)
        wait = random.randint(3, 5)
        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "第", page, "頁:等待", wait, url)
        sleep(wait)
        response = requests.get(url, headers=headers)
        html = BeautifulSoup(response.text)
        products = html.find_all("div", class_="s-include-content-margin")
        # print("本頁商品數量", len(products))
        if len(products) == 0:
            print("沒有商品了", "本次抓取共", page-1, "頁，共", count, "商品")
            break
        for i, product in enumerate(products):
            count += 1
            link = domain + product.find("a", class_="a-link-normal")["href"]
            # link = "https://www.amazon.com/Reebok-CROSSFIT-Flexweave-Cross-Trainer/dp/B073X93KLW/ref=sr_1_14?pf_rd_i=16225019011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=23429fae-990f-41b5-b328-862bb645dd6a&pf_rd_r=Q0C6H7A2Y96W7JT9AXAX&pf_rd_s=merchandised-search-2&pf_rd_t=101&qid=1568863087&rnid=679286011&s=fashion-mens-intl-ship&sr=1-14"
            print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "本次第", count, "筆，第", page, "頁，第", i+1, "件，商品網址", link)
            result = get_page_meta(link)
            columns = list(result.keys())
            if result:
                df = pd.DataFrame(columns=columns)
                data = [result[c] for c in columns]
                s = pd.Series(data, index=columns)
                df = df.append(s, ignore_index=True)
                if os.path.exists(fn):
                    df.to_csv(fn, mode="a", index=False, encoding='utf-8-sig', header=False)
                else:
                    df.to_csv(fn, mode="w", index=False, encoding='utf-8-sig')

            else:
                print("沒有商品內容")
                break
        page += 1
