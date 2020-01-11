import cv2
import numpy as np

def callback(x):
    pass

cap = cv2.VideoCapture("jpvd.mkv")
print("testing...")

cv2.namedWindow('Colorbars')
 
#assign strings for ease of coding
hh='Hue High'
hl='Hue Low'
sh='Saturation High'
sl='Saturation Low'
vh='Value High'
vl='Value Low'
wnd = 'Colorbars'
#Begin Creating trackbars for each
cv2.createTrackbar(hl, wnd,44,179,callback)
cv2.createTrackbar(hh, wnd,70,179,callback)
cv2.createTrackbar(sl, wnd,95,255,callback)
cv2.createTrackbar(sh, wnd,172,255,callback)
cv2.createTrackbar(vl, wnd,158,255,callback)
cv2.createTrackbar(vh, wnd,255,255,callback)



_, frame_orig = cap.read()

while(1):
    frame = frame_orig.copy()
    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # define range of blue color in HSV


    hul=cv2.getTrackbarPos(hl, wnd)
    huh=cv2.getTrackbarPos(hh, wnd)
    sal=cv2.getTrackbarPos(sl, wnd)
    sah=cv2.getTrackbarPos(sh, wnd)
    val=cv2.getTrackbarPos(vl, wnd)
    vah=cv2.getTrackbarPos(vh, wnd)
 
    #make array for final values
    HSVLOW=np.array([hul,sal,val])
    HSVHIGH=np.array([huh,sah,vah])

    #lower_blue = np.array([50,55,55])
    #upper_blue = np.array([60,255,255])
    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange (hsv, HSVLOW, HSVHIGH)

    bluecnts = cv2.findContours(mask.copy(),
                              cv2.RETR_EXTERNAL,
                              cv2.CHAIN_APPROX_SIMPLE)[-2]

    for i in range(0, len(bluecnts)):
        (xg,yg,wg,hg) = cv2.boundingRect(bluecnts[i])
        if hg > 1:
            cv2.rectangle(frame,(xg,yg),(xg+wg, yg+hg),(255,0,9),2)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)
    cv2.imshow('frame',frame)
    #cv2.imshow('mask',mask)
    #cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
