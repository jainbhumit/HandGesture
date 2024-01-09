import mediapipe as mp
import cv2
import webbrowser as wb
cam=cv2.VideoCapture(0)
mph=mp.solutions.hands
mpdraw=mp.solutions.drawing_utils
mpstyle=mp.solutions.drawing_styles



old_counter=0
hand=mph.Hands(min_detection_confidence=0.5,min_tracking_confidence=0.5)
while True :
    r,im=cam.read()
    if r==True :
        im=cv2.flip(im,1)
        results=hand.process(im)
        if results.multi_hand_landmarks:
            counter =0
            for gesture in results.multi_hand_landmarks :
                mpdraw.draw_landmarks(im,gesture,mph.HAND_CONNECTIONS,mpstyle.get_default_hand_landmarks_style(),mpstyle.get_default_hand_connections_style())
                if gesture.landmark[8].y<gesture.landmark[5].y:
                   counter+=1
                if gesture.landmark[12].y<gesture.landmark[9].y:
                   counter+=1    
                if gesture.landmark[16].y<gesture.landmark[13].y:
                   counter+=1
                if gesture.landmark[20].y<gesture.landmark[17].y:
                   counter+=1
            print(counter)
            if counter==2 and old_counter!=counter:
                wb.open('www.google.com')
            if counter==3 and old_counter!=counter:
                wb.open('www.facebook.com')
            old_counter=counter
            

            


        #im=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        #print(im.shape)
        #break
              
        cv2.imshow('user',im)
        if cv2.waitKey(1)&0xff==ord('a') :
            break

cam.release()
cv2.destroyAllWindows()
