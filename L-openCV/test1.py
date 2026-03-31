import cv2
import numpy as np

cap = cv2.VideoCapture(0)
i = 0
while True:
    works, frame = cap.read()
    #COLORFUL FRAME 
    # cv2.imshow('frame', frame)
    print(works , i)
    i+=1

    bw = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # cv2.imshow("New Image", bw)

    # red = cv2.inRange(frame, (0, 0, 100), (100, 100, 255))
    # rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    cv2.imshow('RedFrame', frame)

    if (cv2.waitKey(1) == ord('q')):
        break


cap.release()
cv2.destroyAllWindows()
