#!/usr/bin/env python2

import cv2
import numpy as np
import simplejson as json

cam = cv2.VideoCapture(0)

windows = ['img', 'binary']
for window in windows:
    cv2.namedWindow(window, cv2.CV_WINDOW_AUTOSIZE)

hand_color = json.loads(open('circle.json', 'r').read())
for entry in hand_color:
    hand_color[entry] = np.array(hand_color[entry], np.uint8)

while True:
    _, img = cam.read()
    img = cv2.flip(img, 1)
    hsv = cv2.GaussianBlur(img, (5, 5), 0)
    hsv = cv2.cvtColor(hsv, cv2.COLOR_BGR2HSV)

    binary = cv2.inRange(hsv, hand_color['min'], hand_color['max'])
    binary = cv2.erode(binary, np.ones((5, 5), np.uint8), iterations = 3)

    ret, thresh = cv2.threshold(binary, 127, 255, 0)
    cnt, hie = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    print(len(cnt))
    cv2.drawContours(img, cnt, -1, (0, 255, 0), 3)

    cv2.imshow('img', img)
    cv2.imshow('binary', binary)

    if cv2.waitKey(1) == ord('q') or cv2.waitKey(1) == 27:
        cv2.destroyAllWindows()
        cam.release()
        break
