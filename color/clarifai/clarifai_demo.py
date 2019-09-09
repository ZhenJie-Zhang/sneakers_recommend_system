from clarifai.rest import Image as ClImage
from clarifai.rest import ClarifaiApp
import os
import json

def pic_list(dir_path):
    fs = []
    for f in os.listdir(dir_path) :
        if os.path.isfile(os.path.join(dir_path, f)):
            if "1.jpg" in f:
                fs.append(f)
    # print(fs)
    return fs


dn = "coler_pictures/"
if not os.path.exists(dn):
    os.makedirs(dn)

app = ClarifaiApp(api_key='0f82436fcad44c1cb8953ee52d563ef1')

# model = app.public_models.general_model

model = app.models.get('color')
# picnames = pic_list('D:\clarifai\pictures')

picnames = pic_list('E:\TEAM\\find_color')
# print(picnames)
num = 1
for pics in picnames:
    image = ClImage(filename=pics)
    print("num= ", num)
    print(pics)
    color_list = model.predict([image])["outputs"][0]["data"]["colors"]
    # print(color_list)
    for color in color_list:
        color_id = color["raw_hex"]
        color_pa = color["value"]
        color_name = color["w3c"]["name"]
        print("color_data= ",  color_name, color_id + "\t", str(color_pa * 100)[:5] + "%")
    num += 1