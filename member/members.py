from faker import Faker
import random, string
import pandas as pd
fake = Faker('zh_TW')

columns = ["姓名", "性別", "年齡", "身高","體重","電話","e_mail","註冊時間"]
df = pd.DataFrame(columns=columns)

for _ in range(100):
    print (fake.last_name()+fake.first_name_male(),
           "男",
           random.randint(12,65),
           random.randint(160,188),
           random.randint(48, 100),
           str(0)+str(random.randint(910000000,989999999)),
           fake.free_email(),
           fake.date_time_this_decade(before_now=True, after_now=False, tzinfo=None)
           )

    s = pd.Series([fake.last_name()+fake.first_name_male(),"男",random.randint(12,65),random.randint(160,188),
    random.randint(48, 100),
    str(0)+str(random.randint(910000000,989999999)),
    fake.free_email(),
    fake.date_time_this_decade(before_now=True, after_now=False, tzinfo=None)], index=columns)
    df = df.append(s, ignore_index=True)
    # 輸出CSV
    df.to_csv("members.csv", encoding="utf-8-sig", index=False)



    print(fake.last_name()+fake.first_name_female(),
          "女",
          random.randint(12,65),
          random.randint(148,176),
          random.randint(36, 88),
          str(0)+str(random.randint(910000000,989999999)),
          fake.free_email(),
          fake.date_time_this_decade(before_now=True, after_now=False, tzinfo=None),
          )

    s = pd.Series([fake.last_name()+fake.first_name_female(),"女",random.randint(12,65),random.randint(148,176),
    random.randint(36, 88),
    str(0)+str(random.randint(910000000,989999999)),
    fake.free_email(),
    fake.date_time_this_decade(before_now=True, after_now=False, tzinfo=None)], index=columns)
    df = df.append(s, ignore_index=True)
    # 輸出CSV
    df.to_csv("members.csv", encoding="utf-8-sig", index=False)




