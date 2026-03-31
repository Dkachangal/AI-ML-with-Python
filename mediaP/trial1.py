import mediapipe as mp
import cv2

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

while True:
    works, img = cap.read()

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    result = mp_hands.Hands().process(img)

    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)

    cv2.imshow('FRAME', img)
    if (cv2.waitKey(1) == ord('q')):
        break

cap.release()
cap.destroyAllWindows()