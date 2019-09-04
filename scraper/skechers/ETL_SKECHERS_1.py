import requests
from bs4 import BeautifulSoup
import os
from urllib.request import urlretrieve,time
url = ("https://www.skechers.com/en-us/men/all?genders=M&pageIdx=1")
response = requests.get(url)
html = BeautifulSoup(response.text)
name = html.find_all("p", class_="product-name")
pictures = html.find_all("img", class_="product-component-img")
price = html.find_all("p", class_="price")

for p in name:
    print(p.text)
for q in pictures:
    print(q["srcset"])
for r in price:
    print(r.text)





