#!/usr/bin/env python
# coding: utf8
# author: youdi

import cv2
import numpy as np


def nothing(x):
    pass


# 创建一副黑色图像
img = np.zeros(shape=(300, 512, 3), dtype=np.uint8)

# 命名一个窗口
cv2.namedWindow('image')

# 创建滑动条
cv2.createTrackbar('R', 'image', 0, 255, nothing)
cv2.createTrackbar('G', 'image', 0, 255, nothing)
cv2.createTrackbar('B', 'image', 0, 255, nothing)

# 创建滑动条
switch = '0:0FF\nn1:On'
cv2.createTrackbar(switch, 'image', 0, 1, nothing)

while True:
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    # 获取滑动条的位置
    r = cv2.getTrackbarPos('R', 'image')
    g = cv2.getTrackbarPos('G', 'image')
    b = cv2.getTrackbarPos('B', 'image')
    s = cv2.getTrackbarPos(switch, 'image')

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b, g, r]
cv2.destroyAllWindows()
