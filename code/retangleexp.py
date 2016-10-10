#!/usr/bin/env python
# coding: utf8
# author: youdi

import numpy as np
import cv2

img = np.zeros(shape=(512, 512, 3), dtype=np.uint8)

cv2.retangle(img, (384, 0), (510, 128), (0, 255, 0), 3)
