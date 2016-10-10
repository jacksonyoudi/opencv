#!/usr/bin/env python
# coding: utf8
# author: youdi

import cv2

# 实例化分类器
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

img = cv2.imread('5.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# gray = cv2.imread('test1.jpg', cv2.CV_LOAD_IMAGE_GRAYSCALE)

# detectMultiScale参数解释
# gray, 用于检测的灰度图像
# 1.2: scale_factor 在前后两次相继的扫描中，搜索窗口的比例系数。
#       例如1.1指将搜索窗口依次扩大10%。
# 2: min_neighbors 构成检测目标的相邻矩形的最小个数(缺省－1)。
#       如果组成检测目标的小矩形的个数和小于min_neighbors-1 都会被排除。
#       如果min_neighbors 为 0, 则函数不做任何操作就返回所有的被检候选矩形框。
faces = face_cascade.detectMultiScale(gray, 1.2, 2)
for (x, y, w, h) in faces:
    # cv2.rectangle参数解释
    # (x,y)是矩形左上角
    # (x+w,y+h)是矩形右下角
    # (255,0,0)是矩形的RGB颜色, 为红色
    # 2, 是绘制矩形的线宽
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    roi_gray = gray[y:y + h, x:x + w]
    roi_color = img[y:y + h, x:x + w]
    # 在人脸检测的基础上检测眼睛
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

cv2.imshow('img', img)
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyWindow('test')
