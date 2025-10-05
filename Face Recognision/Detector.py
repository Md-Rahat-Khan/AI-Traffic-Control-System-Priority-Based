import cv2
import numpy as np

cap = cv2.VideoCapture(0)
faceDetect = cv2.CascadeClassifier('haarcascade_frontalface.xml')
rec = cv2.face.LBPHFaceRecognizer_create()
rec.read("recognizer/training.yml")

xd = 0
font = cv2.FONT_HERSHEY_SIMPLEX

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(frame, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        xd, conf = rec.predict(gray[y:y+h, x:x+w])
        if (xd == 1):
            xd = "Rahat"
        cv2.putText(frame, str(xd), (x, y + h + 30), font, 0.55, (0, 255, 0), 1)
    cv2.imshow('Frame', frame)
    if cv2.waitKey(1) == ord('m'):
        break
cap.release()
cv2.destroyAllWindows()