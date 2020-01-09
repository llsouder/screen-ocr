import cv2 as cv
import numpy as np

cap = cv.VideoCapture("jpvd.mkv")
print("testing...")

while(1):

    _, frame = cap.read()
    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # define range of blue color in HSV
    lower_blue = np.array([50,55,55])
    upper_blue = np.array([60,255,255])
    # Threshold the HSV image to get only blue colors
    mask = cv.inRange (hsv, lower_blue, upper_blue)

    bluecnts = cv.findContours(mask.copy(),
                              cv.RETR_EXTERNAL,
                              cv.CHAIN_APPROX_SIMPLE)[-2]

    for i in range(0, len(bluecnts)):
        (xg,yg,wg,hg) = cv.boundingRect(bluecnts[i])
        if hg > 10:
            cv.rectangle(frame,(xg,yg),(xg+wg, yg+hg),(255,0,9),2)

    # Bitwise-AND mask and original image
    res = cv.bitwise_and(frame,frame, mask= mask)
    cv.imshow('frame',frame)
    cv.imshow('mask',mask)
    cv.imshow('res',res)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()
