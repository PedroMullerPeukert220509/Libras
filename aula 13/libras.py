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

      fingers=[]
      dedosFechados = []

      for index in ids:
         
         fingertopy=landmarks[index].y
         fingerbottomy=landmarks[index-2].y

         text=""

         

         if index == 8:
            if fingertopy > fingerbottomy:
               fingers.append(1)

         if index == 12:
            if fingertopy > fingerbottomy:
                fingers.append(1)


         if index != 8 and index != 12:
            if fingertopy < fingerbottomy:
               dedosFechados.append(1)

      if fingers.count(1)==2 and dedosFechados.count(1)>=2:
         letra = []
         letra.append("N")
      
         cv2.putText(image,f"{letra}",(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,250,0),1)


def countfingers2 (image,hand_landmarks,no=0):
   if hands_landmarks:
      landmarks=hand_landmarks[no].landmark

      fingers=[]
      dedosFechados = []

      for index in ids:
         
         fingertopy=landmarks[index].y
         fingerbottomy=landmarks[index-2].y

         text=""

         
       
         fingertopx=landmarks[index].x
         fingerbottomx=landmarks[index-2].x

         if index == 4:
            if fingertopx > fingerbottomx:
               fingers.append(1)

         


         if index != 4: 
            if fingertopy > fingerbottomy:
               dedosFechados.append(1)

      if fingers.count(1)==1 and dedosFechados.count(1)>=4:
         letra = []
         letra.append("A")
      
         cv2.putText(image,f"{letra}",(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,250,0),1)

   


   
           
            
      
      cv2.putText(image,text,(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(250,0,0),1)             
            

      
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
    countfingers2(frame,hands_landmarks)

    cv2.imshow("detector de maos",frame)
    

    if cv2.waitKey(1)==32:
        break
cv2.destroyAllWindows()    

