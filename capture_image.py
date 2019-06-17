#-*-coding:utf-8-*-
import os
import cv2

pth = "/home/exmedl/桌面/灰度人像.jpg"
image = cv2.imread(pth)            #从指定路径读取图像
#image = image.resize(416, 416, 3)
cropImg = image[138:423,126:206] #获取感兴趣区域
cropImg = image[155:401,247:323] #获取感兴趣区域
cv2.imwrite("/home/exmedl/桌面/person2.jpg",cropImg) #保存到指定目录
