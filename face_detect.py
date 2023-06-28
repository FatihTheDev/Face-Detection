import cv2
from random import randrange

trainingData = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

webcam = cv2.VideoCapture(0)

while 1:
    successful_frame, frame = webcam.read()

    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face_coordinates = trainingData.detectMultiScale(grayscaled_img)

    for (x,y,w,h) in face_coordinates:
        rect = cv2.rectangle(frame,(x,y), (x+w,y+h), (0,255,0),4)

    print(cv2.imshow("Face detector", frame))
    key = cv2.waitKey(1)

    if(key == 81 or key == 113):
        break
