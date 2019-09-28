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
# fn = datetime.now().strftime("amazon-%Y%m%d%H%M.csv")
domain = "https://www.amazon.com"
user_agents = [

    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
]

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
    # catgories = html.find("ul", class_="a-unordered-list a-horizontal a-size-small")
    # catgories = ">".join([c.text.strip() for c in catgories.find_all("a")])
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
            # result["catgories"] = catgories
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


def get_allcategory(link):
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
            get_allcategory(result["link"])
            data = {
                "title": result["title"],
                "link": result["link"]
            }
            s = pd.Series(data, index=columns)
            df = df.append(s, ignore_index=True)
    return df


def get_allproduct(url, category):
    fn = datetime.now().strftime("-%Y%m%d%H%M.csv")
    fn = category + fn
    page = 1
    count = 1
    while True:
        headers["user-agent"] = random.choice(user_agents)
        url = url + "&page=" + str(page)
        wait = random.randint(3, 5)
        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "第", page, "頁:等待", wait, url)
        sleep(wait)
        response = requests.get(url, headers=headers)
        html = BeautifulSoup(response.text)
        products = html.find_all("div", class_="s-include-content-margin")
        if len(products) == 0:
            print("沒有商品了", "本次抓取共", page - 1, "頁，共", count, "商品")
            break
        for i, product in enumerate(products):
            link = domain + product.find("a", class_="a-link-normal a-text-normal")["href"]
            print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "本次第", count, "筆，第", page, "頁，第", i + 1, "件，商品網址", link)
            result = get_page_meta(link)
            columns = list(result.keys())
            if result:
                count += 1
                df = pd.DataFrame(columns=columns)
                data = [result[c] for c in columns]
                s = pd.Series(data, index=columns)
                df = df.append(s, ignore_index=True)
                if os.path.exists(fn):
                    df.to_csv(fn, mode="a", index=False, encoding='utf-8-sig', header=False)
                else:
                    df.to_csv(fn, mode="w", index=False, encoding='utf-8-sig')

            else:
                print("抓不到商品內容")
                print(html)
                continue
        page += 1


# 如果子分類存在，繼續尋找子分類，如果子分類不存在，則開始爬取此分類的每一頁
def getsubcategory(link):
    sleep(random.randint(3, 5))
    response = requests.get(link, headers=headers)
    html = BeautifulSoup(response.text)
    data = []
    shoes_catgories = html.find_all("li", class_="s-navigation-indent-2")
    if shoes_catgories:
        for s in shoes_catgories:
            title = s.find("span", class_="a-color-base").text
            link = domain + s.find("a", class_="a-link-normal")["href"]
            result = {
                'title': title,
                'link': link
            }
            data.append(result)

        for d in data:
            print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 'next', d['title'], d['link'])
            getsubcategory(d['link'])
    else:
        category = html.find("li", class_="s-navigation-indent-1").text.strip()
        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 'download', repr(category))
        get_allproduct(link, category)


if __name__ == '__main__':
    link = "https://www.amazon.com/s?i=specialty-aps&bbn=16225019011&rh=n%3A7141123011%2Cn%3A16225019011%2Cn%3A679255011&pf_rd_i=16225019011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=a8717793-9e88-48bb-b385-3487bae57557&pf_rd_p=a8717793-9e88-48bb-b385-3487bae57557&pf_rd_r=A0Y4T1VK1Z4K6VG1HJJN&pf_rd_r=A0Y4T1VK1Z4K6VG1HJJN&pf_rd_s=merchandised-search-left-2&pf_rd_t=101&ref=AE_Men_Shoes"

    # 如果子分類存在，繼續尋找子分類，如果子分類不存在，則開始爬取此分類的每一頁
    getsubcategory(link)
