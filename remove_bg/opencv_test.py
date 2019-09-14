from __future__ import print_function
import numpy as np
import cv2
import PIL.Image as Image
import os
import opencv_test2
# 技術參考:
# https://blog.gtwang.org/programming/opencv-basic-image-read-and-write-tutorial/
# https://blog.csdn.net/qq_40878431/article/details/82941982
# https://www.itread01.com/p/518340.html

# 以第一个像素为准，相同色改为透明

def transparent_back(img):
    img = img.convert('RGBA')
    L, H = img.size
    color_0 = img.getpixel((0, 0))
    print(img.getcolors(L*H)[0])
    for h in range(H):
        for l in range(L):
            dot = (l, h)
            color_1 = img.getpixel(dot)
            if color_1 == color_0:
                color_1 = color_1[:-1] + (0,)
                # print(color_1)
                img.putpixel(dot, color_1)
    return img


def pic_list(dir_path):
    fs = []
    for f in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, f)):
            if "1.jpg" in f:
                fs.append(f)
    # print(fs)
    return fs


if __name__ == '__main__':
    pics = []
    # 讀取檔名最後為 1.jpg 之檔案
    pics = pic_list('E:/TEAM/rm_bg/rm_bg_pic')
    page = 1
    for pic in pics:
        print("第" + str(page) + "張")

        # 讀取檔案路徑
        fn_path = 'E:/TEAM/rm_bg/rm_bg_pic/' + pic
        # 開啟圖檔
        img = Image.open(fn_path)
        # 背景處理
        img = transparent_back(img)

        # print(img.getpixel((50, 50)))
        # img.show(img)
        # 將圖檔存到別的地方，順便轉png黨
        img.save('E:/TEAM/rm_bg/rm_done/' + str(pic)[:-4] + '.png')

        page += 1

        # print(img.getpixel((50, 50))[3])
        # 檢查是否有處理背景，若無 則跑以下程式
        if img.getpixel((50, 50))[3] != 0:
            # 先將背景轉黑
            img2 = opencv_test2.rm_bg_2(fn_path)

            # img2 = cv2.imshow('p', img2)
            # cv2.waitKey(0)

            print('type2')
            # 存檔
            cv2.imwrite('E:/TEAM/rm_bg/rm_done/' + str(pic)[:-4] + '.png', img2)
            # 再取出 做背景透明
            img3 = Image.open('E:/TEAM/rm_bg/rm_done/' + str(pic)[:-4] + '.png')
            img3 = transparent_back(img3)
            # 存檔
            img3.save('E:/TEAM/rm_bg/rm_done/' + str(pic)[:-4] + '.png')


