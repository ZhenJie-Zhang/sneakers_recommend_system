from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import pandas as pd
from time import sleep
import warnings
warnings.filterwarnings('ignore')

#因出現FileNotFoundError: [WinError 2] 系统找不到指定的文件
#按照此文修改設定https://blog.csdn.net/qq_39198486/article/details/82930025
#下載對應版本的chromedriver.exe放到Chrome目錄下的Application裡
#將錯誤訊息中的subprocess.py此檔文件中__init__中的shell=False修改成shell=True
chromedriver_path = "C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe"
driver = webdriver.Chrome(chromedriver_path)
driver.get("http://overdope.com/archives/category/footwear")

#要輸出的CSV格式
columns = ["日期", "標題", "內容", "網址"]
df = pd.DataFrame(columns=columns)


scroll = 0 #selenium捲動計數
start = 0 #文章寫入篇數計數

#selenium捲動的次數
for i in range(200):
    #捲動的JS語法
    #scrollTop的數值必須大於總共捲動的距離
    js="var action=document.documentElement.scrollTop=600000"
    driver.execute_script(js)

    sleep(2)#捲動間休眠
    scroll = scroll + 1 #捲動次數依次+1
    print("捲動第",scroll,"次")

#讀取selenium操作後所呈現的網頁
soup = BeautifulSoup(driver.page_source)

try:
#取出網頁中全部的文章連結
    for r in soup.select("h2", class_="entry-title"):
        url = r.find("a")["href"]

        #寫入篇數依次+1
        start = start + 1

        #讀取各篇文章內容的頁面
        response = requests.get(url).text
        html = BeautifulSoup(response)

        #每讀取1頁休眠1秒
        sleep(1)

        #取出日期
        date = html.find("time", class_="entry-date updated").text

        #取出標題
        title = html.find("h1", class_="entry-title").text

        #取出文章內容
        article = html.find("div", class_="dable-content-wrapper").text

        #寫入CSV格式
        s = pd.Series([date, title, article, url], index=columns)
        df = df.append(s, ignore_index=True)
        print(url,"第",start,"篇", "新增寫入","(",date,")")
        # 輸出CSV
        df.to_csv("overdope_v1.0.csv", encoding="utf-8-sig", index=False)



#錯誤處理
except AttributeError:
     print("寫入第",start,"篇時發生錯誤,略過")
     #在第1282篇 新增寫入時( 2018/06/01 ) http://overdope.com/archives/407790
     #發生404



