#!/usr/bin/env python
# coding: utf8
# author: youdi

import cv2
import numpy as np


# 构建画圆的函数
def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x, y), 100, (255, 0, 0), -1)


# 创建图像与窗口并将窗口与回调函数绑定
img = np.zeros(shape=(512, 512, 3), dtype=np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

while True:
    cv2.imshow('image', img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv.destoryAllWindows()
