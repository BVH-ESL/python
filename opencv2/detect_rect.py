#!/usr/bin/env python

import cv2, argparse
import numpy as np

# construct the argument parser and parse the arguments
#ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", required = True, help = "Path to the image")
#args = vars(ap.parse_args())

#image = cv2.imread(args["image"])
#output = image.copy()
cam = cv2.VideoCapture(0)
while (1):
    ret, image = cam.read()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.bilateralFilter(gray, 11, 17, 17)
    edged = cv2.Canny(gray, 30, 200)
    cv2.imshow('edged', edged)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

#(cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:10]
#screenCnt = None

#for c in cnts:
#    peri = cv2.arcLength(c, True)
#    approx = cv2.approxPolyDP(c, 0.2 * peri, True)
#    if len (approx) == 4 :
#        screenCnt = approx
#        break
#cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 3)
#cv2.imshow("output", image)
#cv2.waitKey(0)
