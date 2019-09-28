# Step0 : import
import pandas as pd
import json
from os import listdir
from os.path import isfile, isdir, join

# Step1: 準備空表格(columns:會先固定住欄位順序)
df = pd.DataFrame(columns=["name", "category", "price", "color", "sizes", "details", "style", "about", "picture", "web"])

# Step2. 準備要插入的資料
##取賣家列表
# 指定要列出所有檔案的目錄
mypath = "E:/python/q86tjp6/xj4wu0_git/shopbop/shopbop"
# 取得所有檔案與子目錄名稱
list_seller = listdir(mypath)
print("mypath:", list_seller)
# a = 0
# b = 0
c = 0
while True:
    try:
        # ##取賣家下的類別列表
        # mypath_seller = "C:/ruten_exshoes/ruten_exshoes_1/ruten/" + list_seller[a]
        # list_category = listdir(mypath_seller)
        # print("mypath_seller:", list_category)
        # ##取賣家下的類別列表
        # mypath_shoes = "C:/ruten_exshoes/ruten_exshoes_1/ruten/" + list_seller[a] +"/"+ list_category[b]
        # list_shoes = listdir(mypath_shoes)
        # print("mypath_shoes:", list_shoes)

        allow = ["json"]
        if list_seller[c].split(".")[-1].lower() in allow:
            dc = "E:/python/q86tjp6/xj4wu0_git/shopbop/shopbop/" + list_seller[c] #+ "/" + list_category[b]+"/"+list_shoes[c]
            print(dc)
            with open(dc, 'r') as f:
                data = json.load(f)
                print(data)
                # dict1 = {"分類":list_category[b],
                #          "賣家":list_seller[a],
                #          "網站":"ruten"}
                #
                # data.update(dict1)
                # print(data)

            # Step3. 插入進去(append)
            # 只要是dataframe專屬功能, 都是屬於第一種(有兩份)
            df = df.append(data, ignore_index=True)
            print("-" * 20)
            print("Item:", c )
            c+=1
        else:
            print("*" * 20)
            print("Item of Picture:", c/2)
            c+=1
    except IndexError:
        print("new category")
        # Step4. 儲存檔案
        # index=False, 不要儲存0,1,2....
        df.to_csv("shopbop_1.csv",
            #list_seller[a] + "_" + list_category[b]+".csv",
                  encoding="utf-8",
                  index=False)
        # print("new category", a, b)
        break

