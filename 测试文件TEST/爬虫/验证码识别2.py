# coding:utf-8
# @Time : 2021/8/26 21:19
# @Author : Micro_tree
# @File : 验证码识别2.py
# @Software : PyCharm
import pytesseract
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

def GrayImage(img):
    """
    功能对图像进行灰度化
    """
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#转化为灰度图
    return img

def ResizeImage(img,ratio):
    """
    功能：重置图片大小
    image_path：图片路径
    ratio：图片的缩放比例
    """
    h, w = img.shape[:2]
    nw,nh = int(ratio*w),int(ratio*h)
    img = cv2.resize(img,(nw,nh))
    return img

def Binarisation(img):
    """
    将图片二值化
    img：待处理的图像
    """
    _,img = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
    return img

def ClearBorder(img):
    """
    功能：去除边框
    """
    h, w = img.shape[:2]
    for y in range(0, w):
        for x in range(0, h):
            if y < 2 or y > w - 2:
                img[x, y] = 255
            if x < 2 or x > h -2:
                img[x, y] = 255
    return img

def interference_line(img):
    """
    功能：线降噪
    """
    h, w = img.shape[:2]
    for y in range(1, w - 1):
        for x in range(1, h - 1):
            count = 0
            if np.all(img[x, y - 1] > 245):
                count = count + 1
            if np.all(img[x, y + 1] > 245):
                count = count + 1
            if np.all(img[x - 1, y] > 245):
                count = count + 1
            if np.all(img[x + 1, y] > 245):
                count = count + 1
            if count > 2:
                img[x, y] = 255
    return img




def Recognition():
    total,true_num = 0,0

    total += 1
    img = cv2.imread('R-C.png')
    img = ResizeImage(img,2)
    img = GrayImage(img)
    img = Binarisation(img)
    img = ClearBorder(img)
    img1 = interference_line(img)
    text = pytesseract.image_to_string(img,lang='eng')

    print(text)
    print("识别准确率为{}".format(true_num/total))

if __name__ == "__main__":
    Recognition()

