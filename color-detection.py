#!/usr/bin/env python2

import cv2
import numpy as np

def nothing(test):
    pass

cam = cv2.VideoCapture(0)

windows = ['hsv', 'raw', 'binary', 'sliders']
for window in windows:
    cv2.namedWindow(window, cv2.CV_WINDOW_AUTOSIZE)

cv2.createTrackbar('h_max', 'sliders', 0, 255, nothing)
cv2.createTrackbar('s_max', 'sliders', 0, 255, nothing)
cv2.createTrackbar('v_max', 'sliders', 0, 255, nothing)

cv2.createTrackbar('h_min', 'sliders', 0, 255, nothing)
cv2.createTrackbar('s_min', 'sliders', 0, 255, nothing)
cv2.createTrackbar('v_min', 'sliders', 0, 255, nothing)

upper = {'h': 0, 's': 0, 'v': 0}
lower = {'h': 0, 's': 0, 'v': 0}

while True:

    for key, val in upper.iteritems():
        upper[key] = cv2.getTrackbarPos(key + '_max', 'sliders')

    for key, val in lower.iteritems():
        lower[key] = cv2.getTrackbarPos(key + '_min', 'sliders')

    _, img = cam.read()
    raw = cv2.flip(img, 1)

    hsv = cv2.GaussianBlur(raw, (5, 5), 0)
    hsv = cv2.cvtColor(hsv, cv2.COLOR_BGR2HSV)

    up = np.array([upper['h'], upper['s'], upper['v']], np.uint8)
    lo = np.array([lower['h'], lower['s'], lower['v']], np.uint8)
    binary = cv2.inRange(hsv, lo, up)

    cv2.imshow('hsv', hsv)
    cv2.imshow('raw', raw)
    cv2.imshow('binary', binary)

    if cv2.waitKey(1) == ord('q') or cv2.waitKey(1) == 27:
        cv2.destroyAllWindows()
        cam.release()
        break
