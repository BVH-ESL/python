import cv2, argparse
import numpy as np

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#gray = np.float32(gray)

dst = cv2.goodFeaturesToTrack(gray, 25, 0.01, 1)
dst = np.int0(dst)
for i in dst:
    x,y = i.ravel()
    cv2.circle(image, (x, y), 3, 255, -1)
#image[dst>0.01*dst.max()] = [0,0,255]
cv2.imshow('gray', gray)
cv2.imshow('dst', image)
if cv2.waitKey(0) & 0xff == 32:
    cv2.destroyAllWindow()
