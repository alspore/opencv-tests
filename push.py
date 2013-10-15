#!/usr/bin/env python2

import cv2
import numpy as np

cam = cv2.VideoCapture(0)

windows = ['raw', 'hsv', 'sliders']

for window in windows:
    cv2.namedWindow(window, cv2.CV_WINDOW_AUTOSIZE)

while True:
    _, img = cam.read()
    img = cv2.flip(img, 1)

    hsv = cv2.GaussianBlur(img, (5, 5), 0)
    hsv = cv2.cvtColor(hsv, cv2.COLOR_BGR2HSV)

    cv2.imshow('raw', img)
    cv2.imshow('hsv', hsv)

    k = cv2.waitKey(1)
    if k == ord('q') or k == 27:
        cv2.destroyAllWindows()
        cam.release()
        break
