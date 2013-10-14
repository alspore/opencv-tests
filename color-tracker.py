#!/usr/bin/env python2

import cv2
import numpy as np

def nothing(test):
    pass

cam = cv2.VideoCapture(0)
cv2.namedWindow('hsv', cv2.CV_WINDOW_AUTOSIZE)
cv2.namedWindow('raw', cv2.CV_WINDOW_AUTOSIZE)
cv2.namedWindow('binary', cv2.CV_WINDOW_AUTOSIZE)

cv2.createTrackbar('upper r', 'binary', 0, 255, nothing)
cv2.createTrackbar('upper g', 'binary', 0, 255, nothing)
cv2.createTrackbar('upper b', 'binary', 0, 255, nothing)

cv2.createTrackbar('lower r', 'binary', 0, 255, nothing)
cv2.createTrackbar('lower g', 'binary', 0, 255, nothing)
cv2.createTrackbar('lower b', 'binary', 0, 255, nothing)

upper = {'r': 0, 'g': 0, 'b': 0}
lower = {'r': 0, 'g': 0, 'b': 0}

while True:

    for key, val in upper.iteritems():
        upper[key] = cv2.getTrackbarPos('upper ' + key, 'binary')

    for key, val in lower.iteritems():
        lower[key] = cv2.getTrackbarPos('lower ' + key, 'binary')

    _, img = cam.read()
    raw = cv2.flip(img, 1)

    hsv = cv2.GaussianBlur(raw, (5, 5), 0)
    hsv = cv2.cvtColor(hsv, cv2.COLOR_BGR2HSV)

    up = np.array([upper['r'], upper['g'], upper['b']], np.uint8)
    lo = np.array([lower['r'], lower['g'], lower['b']], np.uint8)
    binary = cv2.inRange(hsv, lo, up)

    cv2.imshow('hsv', hsv)
    cv2.imshow('raw', raw)
    cv2.imshow('binary', binary)

    if cv2.waitKey(1) == ord('q') or cv2.waitKey(1) == 27:
        cv2.destroyAllWindows()
        cam.release()
        break
