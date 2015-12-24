#!/usr/bin/env python

import cv2, argparse
import numpy as np

# construct the argument parser and parse the arguments
#ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", required = True, help = "Path to the image")
#args = vars(ap.parse_args())

cam = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX
while(cam.isOpened()):
    ret, stream = cam.read()
    resized = cv2.resize(stream, (400, 300), interpolation = cv2.INTER_AREA)
    #image = cv2.imread(args["image"])
    #output = stream.copy()
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

    circles = cv2.HoughCircles(gray, cv2.cv.CV_HOUGH_GRADIENT, 1, 20,
			    param1=50, param2=30, minRadius=5, maxRadius=20)

    #print circles
    if circles is not None :
    #print "654"
        circles = np.round(circles[0, :]).astype("int")
        for (x, y, r) in circles:
            cv2.circle(resized, (x, y), r, (0, 255, 0), 2)
            #cv2.putText(resized, "found circle", (x, y), font, 2, (255, 0, 0), 2)
            #cv2.rectangle(output, (x-5, y-5), (x+5, y+5),(0, 128, 255), -1)
            
    cv2.imshow("output", resized)
    
    k = cv2.waitKey(20)
    if k == 30:
        break
