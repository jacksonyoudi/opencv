#!/usr/bin/env python
# coding: utf8
# author: youdi

import numpy as np
import cv2
from matplotlib import pylab as plt
img = cv2.imread('caiying.png', 0)
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.xticks([]), plt.yticks([])  # to hiede tick values on x anfd Y axis
plt.show()
