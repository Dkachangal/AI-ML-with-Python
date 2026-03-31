import mediapipe as mp
import cv2
import numpy as np

np.array([1, 2, 3, 4])

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
handModel = mp_hands.Hands()
cap = cv2.VideoCapture(0)

cx = 0
cy = 0

while True:
    works, img = cap.read()

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    result = handModel.process(img)

    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    
    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
            h, w, c = img.shape
            print(h, w, c)
            mp_drawing.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)
        for id, lm in enumerate(handLms.landmark):
            cx, cy = int(lm.x * w), int(lm.y *h)
            print(id, cx, cy)
            #CIRCLE AT INDEX FINGER 
            # if (id == 8):
                # cv2.circle(img, (cx, cy), 10, (0, 255, 0), -1)
            
            #Cube in palm
            if (id == 0):
                cx -= 10
                cy -= 10
                points = np.array([(cx, cy), (cx - 50, cy), (cx - 50, cy - 50), (cx, cy - 50)])
                # points = np.array([cx, cy], ())
                cv2.polylines(img, [points], True, (0, 255, 0), 2)



    img = cv2.flip(img, 1)
    img = cv2.resize(img, (900, 600))
    cv2.imshow('FRAME', img)
    if (cv2.waitKey(1) == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()