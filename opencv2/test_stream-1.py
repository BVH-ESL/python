import cv2
import time

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 1024)
time.sleep(2)
cap.set(15, 0.1)

while True:
    ret, img = cap.read()
    cv2.imshow("input", img)
    key = cv2.waitKey(10)
    if key == 27:
        break

cv2.destroyAllWindows()
cv2.VideoCapture(0).release()
