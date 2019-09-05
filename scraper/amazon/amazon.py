from bs4 import BeautifulSoup
from time import sleep
import requests
import os
import random
import warnings

warnings.filterwarnings('ignore')

dn = "amazon/"

page = 2

# url = "https://www.amazon.com/s?k=%E9%9E%8B&currency=TWD&ref=nb_sb_noss"
while True:
    url = "https://www.amazon.com/s?k=鞋&page=" + str(page) + "&currency=TWD&qid=1567664498&ref=sr_pg_" + str(page)
    print(url)
    headers = {
        "accept-language": "zh-TW,zh;q=0.9,ja-JP;q=0.8,ja;q=0.7,en-US;q=0.6,en;q=0.5",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/76.0.3809.132 Safari/537.36 "
    }
    # try:
    response = requests.get(url, headers=headers).text
    html = BeautifulSoup(response)
    # print(html)
    product = html.find_all('div', class_='s-expand-height s-include-content-margin s-border-bottom')

    picture = [[pic.split(' ')[0]
                for pic in str(pics.find('img', class_='s-image')['srcset']).split(', ')]
               for pics in product]
    print(len(picture))

    for i, p in enumerate(picture):
        fn = p[0].split('/')[-1]
        print(i, p[0], fn)
        # try:
        # response = requests.get(p[0], stream=True)

        # except Exception as e:
        #     print(e.with_traceback())
        #     print("不能下載")

        # if not os.path.exists(dn):
        #     os.makedirs(dn)
        #
        # f = open(dn + fn, "wb")
        # f.write(response.raw.read())
        # f.close()
        # sleep(random.randint(1, 3))

    page += 1

    # except Exception as e:
    #     print(e.__traceback__)
    #     print("共", page - 1, "頁")
    #     break
