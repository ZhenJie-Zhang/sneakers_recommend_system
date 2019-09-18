from bs4 import BeautifulSoup
from time import sleep
import requests
import os
import random
import warnings

warnings.filterwarnings('ignore')

dn = "./amazon/"

page = 1
count = 0
download = 0

file_list = os.listdir(dn)

# url = "https://www.amazon.com/s?k=%E9%9E%8B&currency=TWD&ref=nb_sb_noss"
while True:
    # url = "https://www.amazon.com/s?k=鞋&page=" + str(page) + "&currency=TWD&qid=1567664498&ref=sr_pg_" + str(page)
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

    headers = {
        "accept-language": "zh-TW,zh;q=0.9,ja-JP;q=0.8,ja;q=0.7,en-US;q=0.6,en;q=0.5",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/76.0.3809.132 Safari/537.36 "
    }

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
    # 停在這一頁：https://www.amazon.com/
        # s?i=fashion-mens-intl-ship&bbn=16225019011&rh=n
        # %3A16225019011%2Cn%3A679255011%2Cn%3A6127770011%2Cn
        # %3A679286011&dc&page=59&pf_rd_i=16225019011
        # &pf_rd_m=ATVPDKIKX0DER&pf_rd_p=23429fae-990f-41b5-b328-862bb645dd6a
        # &pf_rd_r=1DZK4TJYM27GRZNZSF72&pf_rd_s=merchandised-search-2&pf_rd_t=101&
        # qid=1567740449&rnid=6127770011&ref=sr_pg_59