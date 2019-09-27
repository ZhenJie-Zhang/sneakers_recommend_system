# use excel save to .csv
import pandas as pd
# first read_csv in encoding = "目前的code"
# file_from = "./ruten.csv"  #<--where is file from
file_from = eval(input("where is file from (ex:'./ruten.csv'): "))
df = pd.read_csv(file_from, encoding = "950") # find encoding to decoding file
print(df)
print(df.columns) # check columns
print("-"*20)
# second change encoding = "utf-8-sig" to save(to_csv)
# new_encoding_file = "./ruten_1.csv" #<-- new file
new_encoding_file = eval(input("where does new file save to (ex:'./ruten_1.csv'): "))
df1 = df.to_csv(new_encoding_file, encoding = "utf-8-sig", index = False)
print("-"*20)
# third check to decoding file
df2 = pd.read_csv(new_encoding_file, encoding = "utf-8-sig")
print(df2)
print(df.columns) # check columns
