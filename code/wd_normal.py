#!/usr/bin/env python
# coding: utf8
# author: youdi

import numpy as np
import cv2

img = cv2.imread('../img/2.jpg', 1)
cv2.namedWindow('img', cv2.WINDOW_NORMAL)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('hangcaiying.png', img)
