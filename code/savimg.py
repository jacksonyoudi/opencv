#!/usr/bin/env python
# coding: utf8
# author: youdi
import cv2
import numpy as np


img = cv2.imread('../img/3.jpg', 0)
cv2.imshow('image', img)
k = cv2.waitKey(0)
if k == 27:  # wait for ECS key exit
    cv2.destroyAllWindows()
elif k == ord('s'):  # wait for 's' key to save and exit
    cv2.imwrite('hang.png', img)
    cv2.destroyAllWindows()
