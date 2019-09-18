import requests
from bs4 import BeautifulSoup
from time import sleep
from warnings import filterwarnings
filterwarnings("ignore")


url = "https://www.amazon.com/s/ref=s9_acss_bw_cts_AEMFVNEN_T2_w?rh=n%3A7141123011%2Cn%3A16225019011%2Cn%3A679255011&bbn=16225019011&ie=UTF8&pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-2&pf_rd_r=ZPB6CPW1HEKWPTB6P5JP&pf_rd_t=101&pf_rd_p=23429fae-990f-41b5-b328-862bb645dd6a&pf_rd_i=16225019011"

headers = {
        "accept-language": "zh-TW,zh;q=0.9,ja-JP;q=0.8,ja;q=0.7,en-US;q=0.6,en;q=0.5",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/76.0.3809.132 Safari/537.36 "
    }

response = requests.get(url, headers=headers)
html = BeautifulSoup(response.text)

shoes_catgories = html.find_all("li", class_="s-navigation-indent-2")

for s in shoes_catgories:
    title = s.find("span", class_="a-color-base").text
    link = s.find("a", class_="a-link-normal")["href"]
    print(title, link)