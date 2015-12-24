#!/usr/bin/env python

import cv2, argparse
import numpy as np

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
output = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.bilateralFilter(gray, 11, 17, 17)
kernel = np.ones((5, 5), np.uint8)
edged = cv2.Canny(gray, 30, 200)
edged = cv2.dilate(edged, kernel, iterations = 1)
edged = cv2.erode(edged, kernel, iterations = 1)
#edged = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)
minLineLength = 10 
maxLineGap = 1 
lines = cv2.HoughLinesP(edged, 1, np.pi/180, 200) 
print lines
#for x1, y1, x2, y2 in lines[0]:
#    cv2.lines(output, (x1, y1), (x2, y2), (255, 0, 0), 2)

while (1):
    #cv2.imshow('input', image)
    cv2.imshow('edge', edged)
    #cv2.imshow('output', output)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()


