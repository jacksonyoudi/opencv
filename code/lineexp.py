#!/usr/bin/env python
# coding: utf8
# author: youdi

import numpy as np
import cv2

# 创建一个黑背景的图
img = np.zeros(shape=(512, 512, 3), dtype=np.uint8)

# line(画布，起点，终点，颜色，宽度)
cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)
