import cv2
from random import randrange

trainingData = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

webcam = cv2.VideoCapture(0)

while 1:

    successful_frame, frame = webcam.read()

    # convert the frame to grayscale
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Get the size of the text
    (text_width, text_height), _ = cv2.getTextSize("Text", cv2.FONT_HERSHEY_SIMPLEX, 3, 4)

    # Calculate the position of the text
    x = frame.shape[1] - text_width - 170 
    y = frame.shape[0] - text_height + 30 
    cv2.putText(frame, "Face detection by FatihTheDev", (x, y), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.7, color=(255, 255, 255), thickness=2)

    # get the face coordinates
    face_coordinates = trainingData.detectMultiScale(grayscaled_img)

    # draw a rectangle  
    for (x,y,w,h) in face_coordinates:
        rect = cv2.rectangle(frame,(x,y), (x+w,y+h), (0,255,0),4)

    # show video
    print(cv2.imshow("Face detector", frame))
    key = cv2.waitKey(1)

    if(key == 81 or key == 113):
        break
        
webcam.release()
cv2.destroyAllWindows  
