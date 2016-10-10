#!/usr/bin/env python
# coding: utf8
# author: youdi


import numpy as np
import cv2
# 创建一个黑背景的图
img = np.zeros(shape=(512, 512, 3), dtype=np.uint8)

# 画布，圆心，半径，颜色，粗细
cv2.circle(img, (447, 63), 63, (0, 0, 255), -1)
