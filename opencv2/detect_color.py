#!/usr/bin/env python

import cv2, argparse
import numpy as np

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
output = image.copy()

# Convert BGR to HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# define range of blue color in HSV
lower_blue = np.array([50,50,50])
upper_blue = np.array([70,255,255])

# Threshold the HSV image to get only blue colors
mask = cv2.inRange(hsv, lower_blue, upper_blue)

while(1):
    cv2.imshow('mask', mask)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
