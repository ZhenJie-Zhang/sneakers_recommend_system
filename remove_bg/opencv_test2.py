from __future__ import print_function
import numpy as np
import cv2
from matplotlib import pyplot as plt

def rm_bg_2(fn_path):
    img = cv2.imread(fn_path)
    mask = np.zeros(img.shape[:2], np.uint8)
    bgdModel = np.zeros((1, 65), np.float64)
    fgdModel = np.zeros((1, 65), np.float64)
    rect = (50, 50, 450, 290)
    # 劃定區域
    cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
    # 函式返回值為mask,bgdModel,fgdModel
    mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
    # 0和2做背景
    img = img*mask2[:, :, np.newaxis]
    return img
    # 使用蒙板來獲取前景區域
    # cv2.imshow('p', img)
    # cv2.waitKey(0)