#!/usr/bin/env python

import cv2
import numpy as np

capture = cv2.VideoCapture('video.mp4')
while capture.isOpened():

    ret, frame =capture.read()

    img = frame
    scale = 60
    width = int(img.shape[1] * scale / 100)
    height = int(img.shape[0] * scale / 100)
    dim = (width, height) 
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    frame = resized

    blurred_frame = cv2.GaussianBlur(frame, (5,5), 0) 

    HSV = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)
    color_l = np.array([60, 150, 110])
    color_h = np.array([91, 255,255])
    mask=cv2.inRange(HSV, color_l, color_h)
    contours, _= cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 1000:
            cv2.drawContours(frame,contour,-1,(255,0,255),3)

    cv2.imshow('',frame)
    if cv2.waitKey(30) & 0xFF ==ord('a'):
        break
capture.release()
cv2.destroyAllWindows()
