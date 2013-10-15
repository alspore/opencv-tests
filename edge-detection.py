#!/usr/bin/env python2

import cv2

cam = cv2.VideoCapture(0)

windows = ['raw', 'edges']

for window in windows:
    cv2.namedWindow(window, cv2.CV_WINDOW_AUTOSIZE)

while True:
    _, img = cam.read()
    img = cv2.flip(img, 1)

    edges = cv2.Canny(img, 100, 150)

    cv2.imshow('raw', img)
    cv2.imshow('edges', edges)

    k = cv2.waitKey(1)
    if k == ord('q') or k == 27:
        cv2.destroyAllWindows()
        cam.release()
        break
