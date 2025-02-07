import cv2 as cv
import numpy as np
cap=cv.VideoCapture(0)
while(True):
    rec,frame=cap.read()
    frame_hsv=cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    lower_red=np.array([0,50,50])
    upper_red=np.array([255,255,180])
    mask_red=cv.inRange(frame_hsv,lower_red,upper_red)
    cv.imshow("webcam",frame)
    cv.imshow("maskred",mask_red)
    key_exit=cv.waitKey(5)& 0xFF
    if key_exit==27:
        break
cv.destroyWindow()
cap.releas()