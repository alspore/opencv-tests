#!/usr/bin/env python2

import numpy as np
import cv2

cap = cv2.VideoCapture(0)
orb = cv2.ORB()

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    kp = orb.detect(frame, None)

    img = cv2.drawKeypoints(frame, kp, color=(0, 255, 0), flags=0)

    cv2.imshow('frame', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

