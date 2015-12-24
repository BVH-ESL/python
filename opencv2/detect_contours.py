#!/usr/bin/env python

import cv2, argparse
import numpy as np

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
output = image.copy()
image = cv2.medianBlur(image, 3)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.bilateralFilter(gray, 11, 17, 17)
kernel = np.ones((5, 5), np.uint8)
edged = cv2.Canny(gray, 30, 200)
edged = cv2.dilate(edged, kernel, iterations = 1)
edged = cv2.erode(edged, kernel, iterations = 1)
#edged = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)
ret, thresh = cv2.threshold(edged, 0, 255, 0)

contours, h = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

font = cv2.FONT_HERSHEY_SIMPLEX
for cnt in contours:
    approx = cv2.approxPolyDP(cnt, 0.1*cv2.arcLength(cnt, False), True)
    #print len(approx)
    print approx[0][0][1]
    cv2.putText(edged, str(len(approx)), (approx[0][0][0], approx[0][0][1]+20), font, 1, (255, 255, 255), 1, cv2.CV_AA)
    if len(approx) == 9:
        cv2.drawContours(output, [cnt], 0, (0, 0, 255), -1)
    elif len(approx) == 8:
        cv2.drawContours(output, [cnt], 0, (0, 255, 0), -1)
    elif len(approx) <=4 :
        cv2.drawContours(output, [cnt], 0, (255, 0, 0), -1)
while (1):
    cv2.imshow('input', image)
    cv2.imshow('edge', edged)
    cv2.imshow('output', output)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()


