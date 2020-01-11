import cv2 as cv
import numpy as np

def callback(x):
    pass

cap = cv.VideoCapture("jpvd.mkv")
print("testing...")

cv.namedWindow('Colorbars')
 
#assign strings for ease of coding
hh='Hue High'
hl='Hue Low'
sh='Saturation High'
sl='Saturation Low'
vh='Value High'
vl='Value Low'
wnd = 'Colorbars'
#Begin Creating trackbars for each
cv.createTrackbar(hl, wnd,44,179,callback)
cv.createTrackbar(hh, wnd,70,179,callback)
cv.createTrackbar(sl, wnd,95,255,callback)
cv.createTrackbar(sh, wnd,172,255,callback)
cv.createTrackbar(vl, wnd,158,255,callback)
cv.createTrackbar(vh, wnd,255,255,callback)



_, frame_orig = cap.read()

while(1):
    frame = frame_orig.copy()
    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # define range of blue color in HSV


    hul=cv.getTrackbarPos(hl, wnd)
    huh=cv.getTrackbarPos(hh, wnd)
    sal=cv.getTrackbarPos(sl, wnd)
    sah=cv.getTrackbarPos(sh, wnd)
    val=cv.getTrackbarPos(vl, wnd)
    vah=cv.getTrackbarPos(vh, wnd)
 
    #make array for final values
    HSVLOW=np.array([hul,sal,val])
    HSVHIGH=np.array([huh,sah,vah])

    #lower_blue = np.array([50,55,55])
    #upper_blue = np.array([60,255,255])
    # Threshold the HSV image to get only blue colors
    mask = cv.inRange (hsv, HSVLOW, HSVHIGH)

    bluecnts = cv.findContours(mask.copy(),
                              cv.RETR_EXTERNAL,
                              cv.CHAIN_APPROX_SIMPLE)[-2]

    for i in range(0, len(bluecnts)):
        (xg,yg,wg,hg) = cv.boundingRect(bluecnts[i])
        if hg > 1:
            cv.rectangle(frame,(xg,yg),(xg+wg, yg+hg),(255,0,9),2)

    # Bitwise-AND mask and original image
    res = cv.bitwise_and(frame,frame, mask= mask)
    cv.imshow('frame',frame)
    #cv.imshow('mask',mask)
    #cv.imshow('res',res)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()
