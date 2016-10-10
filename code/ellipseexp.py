#!/usr/bin/env python
# coding: utf8
# author: youdi

import numpy as np
import cv2

img = np.zeros(shape=(512, 512, 3), dtype=np.uint8)
cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 180, 255, -1)
