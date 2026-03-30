import cv2
import numpy as np

cap = cv2.VideoCapture(0)
i = 0
while True:
    works, frame = cap.read()
    cv2.imshow('frame', frame)
    print(works , i)
    i+=1

    if (cv2.waitKey(1) == ord('q')):
        break


cap.release()
cv2.destroyAllWindows()
