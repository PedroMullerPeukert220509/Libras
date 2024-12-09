import cv2
import mediapipe as mp

cap=cv2.VideoCapture(0)

mp_hands=mp.solutions.hands
mp_bones=mp.solutions.drawing_utils

hands=mp_hands.Hands(min_detection_confidence=0.8,min_tracking_confidence=0.5)

ids=[4,8,12,16,20]

def countfingers (image,hand_landmarks,no=0):
   if hands_landmarks:
      landmarks=hand_landmarks[no].landmark

      fingers=0

      for index in ids:
         
         fingertopy=landmarks[index].y
         fingerbottomy=landmarks[index-2].y

         fingertopx=landmarks[index].x
         fingerbottomx=landmarks[index-2].x

         if index ==4:
            if fingertopy<fingerbottomy:
               fingers=1
               print(index,"like")
            if fingertopy>fingerbottomy:
               fingers=2
               print(index,"dislike") 
        #  else:
        #     if fingertopx>fingerbottomx:
        #        fingers.append(1)
        #        print(index,"esta aberto")
        #     if fingertopx<fingerbottomx:
        #        fingers.append(0)
        #        print(index,"esta fechado") 

      
      if fingers==1:
         text= f"like"
         cv2.putText(image,text,(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,250,0),1) 
     
      elif fingers==2:   
        text= f"dislike"
        cv2.putText(image,text,(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,250),1)    
            

      
def drawHandLanmarks(image, hand_landmarks):

    # Desenhar as conexões entre os pontos de referência
    if hand_landmarks:

      for landmarks in hand_landmarks:
               
        mp_bones.draw_landmarks(image, landmarks, mp_hands.HAND_CONNECTIONS)
while True:
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)

    result=hands.process(frame)

    hands_landmarks=result.multi_hand_landmarks
    drawHandLanmarks(frame,hands_landmarks)
    countfingers(frame,hands_landmarks)

    cv2.imshow("detector de maos",frame)
    print(hands_landmarks)

    if cv2.waitKey(1)==32:
        break
cv2.destroyAllWindows()    

