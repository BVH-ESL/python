#!/usr/bin/env python

import cv2, time, os

start_time = time.time()
current_time = time.time()
path = "../home/pi/Desktop/4Floor"
path += time.ctime()
os.makedirs(path)
    
#cv2.namedWindow("lll")
cam = cv2.VideoCapture(0)
while(1) :
    ret,img = cam.read()
    #dim = (1280, 720) #width, high
    #resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    
    if time.time()-current_time > 5:        
        print time.ctime()
        name = time.ctime()+".jpg"
        #print name
        cv2.imwrite(path+"/"+name, img)
        current_time = time.time()
