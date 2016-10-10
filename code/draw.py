#!/usr/bin/env python
# coding: utf8
# author: youdi


import numpy as np
import cv2

# 创建一个黑背景的图
img = np.zeros(shape=(512, 512, 3), dtype=np.uint8)

# line(画布，起点，终点，颜色，宽度)
cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)

# 画布，圆心，半径，颜色，粗细
cv2.circle(img, (447, 63), 63, (0, 0, 255), -1)

cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)
cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 180, 255, -1)

pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
pts = pts.reshape((-1, 1, 2))

# 定义字体类型
font = cv2.FONT_HERSHEY_SIMPLEX
# putText(画布，内容，位置，字体类型，
cv2.putText(img, 'OpenCV', (10, 500), font, 4, (255, 255, 255), 2)

winname = 'example'
cv2.namedWindow(winname)
cv2.imshow(winname, img)
cv2.waitKey(0)
cv2.destroyWindow(winname)
