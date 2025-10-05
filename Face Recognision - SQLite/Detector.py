import cv2
import numpy
from PIL import Image
import pickle
import sqlite3

#cap = cv2.VideoCapture(1)
cap = cv2.VideoCapture(0)
faceDetect = cv2.CascadeClassifier('haarcascade_frontalface.xml')
rec = cv2.face.LBPHFaceRecognizer_create()
rec.read("recognizer/training.yml")

def getProfile( xd ):
    conn = sqlite3.connect("FaceBase.db")
    cmd = "SELECT * FROM Persons where ID ="+str(xd)
    cursor = conn.execute(cmd)
    profile = None
    for row in cursor:
        profile = row
    conn.close()
    return profile

xd = 0
font = cv2.FONT_HERSHEY_SIMPLEX

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(frame, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        xd, conf = rec.predict(gray[y:y+h, x:x+w])
        profile = getProfile(xd)
        if profile!= None:
            cv2.putText(frame, str(profile[1]), (x, y+h+30), font, 0.55, (0, 255, 0), 1)
            cv2.putText(frame, str(profile[2]), (x, y+h+60), font, 0.55, (0, 255, 0), 1)
            cv2.putText(frame, str(profile[3]), (x, y+h+90), font, 0.55, (0, 255, 0), 1)
            cv2.putText(frame, str(profile[4]), (x, y+h+120), font, 0.55, (0, 255, 0), 1)
    cv2.imshow('Frame', frame)
    if cv2.waitKey(1) == ord('m'):
        break
cap.release()
cv2.destroyAllWindows()


