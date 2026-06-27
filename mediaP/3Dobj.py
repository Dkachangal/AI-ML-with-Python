import cv2
import mediapipe as mp
import numpy as np

cap = cv2.VideoCapture(0)
mp_hands = mp.solutions.hands
handModule = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils

cx = 0
cy = 0
boxThickness = 2

while True:
    #start capturing video img by img
    works, img = cap.read()
    
    #resize the image
    img = cv2.resize(img, (1230, 720))

    #convert BGR to RGB
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # DRAW 4 RECTANGULAR BOXES ON THE TOP OF HEIGHT 100PX
    # box 1
    box1 = np.array([(0, 0), (0, 100), (306, 100), (306, 0)])
    img = cv2.polylines(img, [box1], True, (255, 0, 0), boxThickness)
    # box 2
    box2 = np.array([(0+308, 0), (0+308, 100), (306+308, 100), (306+308, 0)])
    img = cv2.polylines(img, [box2], True, (0, 255, 0), boxThickness)
    # box 3
    box3 = np.array([(0+308+308, 0), (0+308+308, 100), (306+308+308, 100), (306+308+308, 0)])
    img = cv2.polylines(img, [box3], True, (0, 0, 255), boxThickness)
    # box 4
    box4 = np.array([(0+308+308+308, 0), (0+308+308+308, 100), (306+308+308+308, 100), (306+308+308+308, 0)])
    img = cv2.polylines(img, [box4], True, (0, 0, 0), boxThickness)

    result = handModule.process(img)

    if result.multi_hand_landmarks:

        # for each hand detected, draw the landmarks and connections
        for handLms in result.multi_hand_landmarks:
            h, w, c = img.shape
            mp_drawing.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)

        # GETTING THE HAND LOCATION AT INSTANT
        for id, lm in enumerate(handLms.landmark):
            cx = int(lm.x * w)
            cy = int(lm.y * h)
            x1 = int(lm.x * w)  #x1
            y1 = int(lm.y * h)  #y1
            x2 = int(lm.x * w)  #x2
            y2 = int(lm.y * h)  #y2
            # DRAWING LINE BETWEEN INDEX AND INDEX
            # scan if id of index detected
            # if (hand_label.classification[0].label)
            if (result.multi_handedness):
                for hand_label in result.multi_handedness:
                    # GIVES OPPOSITE (LEFT FOR RIGHT AND RIGHT FOR LEFT)
                    if (hand_label.classification[0].label == "Left"):
                        # RIGHT HAND
                        if (id == 8):
                            # get all coordinates
                            x2 = int(lm.x * w)  #x2
                            y2 = int(lm.y * h)  #y2
                            
                    if (hand_label.classification[0].label == "Right"):
                        # LEFT HAND
                        if (id == 8):
                            x1 = int(lm.x * w)  #x1
                            y1 = int(lm.y * h)  #y1
                    # now draw a line beteween those coordinates
                    # use while loop

                    # m = y2 - y1 / x2 - x1
                    if (x2 == x1):
                        m = 0.5
                    else:
                        m = (y2 - y1) / (x2 - x1)

                    while (x2 != x1 and y2 != y1):
                        # y++, x++
                        # y++, x--
                        # y--, x++
                        # y--, x--

                        # eqn of line 
                        # y - y1 = ( x - x1 ) * m
                        y2 += 1
                        x2 += 1
                        if ((y2 - y1) == (x2 - x1)*m):
                            # point is on the line
                            # draw circle
                            cv2.circle(img, (x2, y2), 10, (0, 255, 0), -1)
                            continue
                            # continue the loop (from top - dont go to bottom)
                            # continue
                        # taking y++, x--
                        x2 -= 2
                        if ((y2 - y1) == (x2 - x1)*m):
                            # point is on the line
                            # draw circle
                            cv2.circle(img, (x2, y2), 10, (0, 255, 0), -1)
                            continue
                            # continue the loop (from top - dont go to bottom)
                            # continue
                        
                        # now taking y-- x++
                        y2 -= 2
                        x2 += 2
                        if ((y2 - y1) == (x2 - x1)*m):
                            # point is on the line
                            # draw circle
                            cv2.circle(img, (x2, y2), 10, (0, 255, 0), -1)
                            continue
                            # continue the loop (from top - dont go to bottom)
                            # continue

                        # now taking y-- x--
                        y2 += 2
                        if ((y2 - y1) == (x2 - x1)*m):
                            # point is on the line
                            # draw circle
                            cv2.circle(img, (x2, y2), 10, (0, 255, 0), -1)
                            continue
                            # continue the loop (from top - dont go to bottom)
                            # continue
            
                            




            # INCREASE THICKNESS ON HOVER
            if (cx <=306+308+308+308 and cx >0+308+308+308 and cy<100 and cy > 0 and id == 8):
                img = cv2.polylines(img, [box4], True, (0, 0, 0), boxThickness+5)

            if (cx <=0+308+308+308 and cx >0+308+308 and cy<100 and cy > 0 and id == 8):
                img = cv2.polylines(img, [box3], True, (0, 0, 255), boxThickness+5)

            if (cx <=0+308+308 and cx >0+308 and cy<100 and cy > 0 and id == 8):
                img = cv2.polylines(img, [box2], True, (0, 255, 0), boxThickness+5)


            if (cx <=0+308 and cx >0 and cy<100 and cy > 0 and id == 8):
                img = cv2.polylines(img, [box1], True, (255, 0, 0), boxThickness+5)

            # drawing a cube in the right palm
            if (id == 0):
                cx -= 10
                cy -= 10
                points = np.array([(cx, cy), (cx + 50, cy), (cx + 50, cy - 50), (cx, cy - 50)])
                img = cv2.polylines(img, [points], True, (235, 50, 140), 4)

    # flip the image
    img = cv2.flip(img, 1)

    # img RGB to BGR
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    #display the image
    cv2.imshow('FRAME', img)

    # Exit on 'q press
    if (cv2.waitKey(1) == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()