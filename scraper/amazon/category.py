import requests
import random
import pandas as pd
from bs4 import BeautifulSoup
from time import sleep
from warnings import filterwarnings
filterwarnings("ignore")

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
            "cookie": """aws-priv=eyJ2IjoxLCJldSI6MCwic3QiOjB9; aws-target-static-id=1560494069657-81731; aws-target-data=%7B%22support%22%3A%221%22%7D; s_fid=23702F43EBBB5D20-0568221326992E2C; session-id=145-6873007-2152334; session-id-time=2082787201l; sp-cdn="L5Z9:TW"; ubid-main=131-8626244-2372658; x-wl-uid=18jEl9ECOsUrDVk3Au9lytr0gRo2T27A1zaI43UJo4xDbaeja4TedUg9OVvxGMrLIVt4UFmN9IAg=; skin=noskin; aws_lang=tw; s_cc=true; aws-target-visitor-id=1560494069660-96739.22_33; aws-mkto-trk=id%3A112-TZM-766%26token%3A_mch-aws.amazon.com-1568612464248-31828; aws-ubid-main=910-8675238-8373003; aws-business-metrics-last-visit=1568612619561; aws-account-alias=cxcxc-learning; aws-userInfo=%7B%22arn%22%3A%22arn%3Aaws%3Aiam%3A%3A129729052534%3Auser%2Fstudent19%22%2C%22alias%22%3A%22cxcxc-learning%22%2C%22username%22%3A%22student19%22%2C%22keybase%22%3A%22l%2B3axisItfjK5KoE1zY0kfUaAUU42loMUG%2F%2FPRyWKLU%5Cu003d%22%2C%22issuer%22%3A%22http%3A%2F%2Fsignin.aws.amazon.com%2Fsignin%22%7D; regStatus=registered; aws-session-id=482-0013835-5519685; c_m=undefinedwww.google.comSearch%20Engine; s_sq=%5B%5BB%5D%5D; noflush_locale=en; s_vn=1592030069812%26vn%3D4; s_dslv=1568615377984; s_nr=1568615377990-Repeat; aws-session-id-time=1568621919l; lc-main=zh_TW; session-token=/oa0n2LH5YXoIOEk9gqdkzUUyQCdhRqnh1lu0HjugXbKf4PH8MK0Xip3ozlqeZDVdGKk4rYl3flc0+X8hBcRFli7w7K94LXavKhz3J9zYzFFhr4JEyUUVSkiE9JMi9pgp0sL9gEPEoTYahERKsNTVg5aEyFsDsPMP9l1T3Baa48osvRtT/7BhPgGqTh5vI+W; i18n-prefs=TWD; csm-hit=tb:s-Y0QAE0WZ3PMC4HFQ92RH|1568864879948&t:1568864881231&adb:adblk_no""",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "same-origin",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1"
        }


def get_manfashion(url):
    headers["user-agent"] = random.choice(user_agents)
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


def get_category(urls):
    df = pd.DataFrame()
    for url in urls:
        headers["user-agent"] = random.choice(user_agents)
        wait = random.randint(3, 5)
        print(wait)
        sleep(wait)
        response = requests.get(url, headers=headers)
        html = BeautifulSoup(response.text)
        result = {}
        shoes_catgories = html.find_all("li", class_="s-navigation-indent-2")
        for s in shoes_catgories:
            title = s.find("span", class_="a-color-base").text
            link = domain + s.find("a", class_="a-link-normal")["href"]
            result["title"] = title
            result["link"] = link
            columns = list(result.keys())
            if result:
                data = [result[c] for c in columns]
                s = pd.Series(data, index=columns)
                df = df.append(s, ignore_index=True)
    return df


if __name__ == '__main__':
    catgory = pd.read_csv("shoes_catgory_all.csv", encoding="utf-8-sig")
    print(catgory["title"].tolist())
    print(catgory["link"].tolist())
    links = catgory["link"].tolist()
    # print(catgory)
    print(catgory.iloc[[0]])
    # catgory_s = get_category(links)
    # print(catgory_s)
    # catgory_s.to_csv("shoes_catgory_all.csv", encoding="utf-8-sig", index=True, index_label="id")
