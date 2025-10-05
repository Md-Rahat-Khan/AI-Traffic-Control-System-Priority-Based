import cv2
import sqlite3

cap = cv2.VideoCapture(0)
faceDetect = cv2.CascadeClassifier('haarcascade_frontalface.xml')

def insertOrUpdate(Id, Name, Gender, Age):
    conn = sqlite3.connect("FaceBase.db")
    cmd = "SELECT * FROM Persons where ID=" + str(Id)
    cursor = conn.execute(cmd)
    isExist = 0
    for r in cursor:
        isExist = 1
    if isExist == 1:
        cmd = "UPDATE Persons SET Name =" + str(Name) + "Gender =" + str(Gender) + "Age =" + str(Age) + "where ID=" + str(Id)
    else:
        cmd = "INSERT INTO Persons(ID, Name, Gender, Age) Values (" + str(Id) + "," + str(Name) + "," + str(Gender) + "," + str(Age) + ")"
    conn.execute(cmd)
    conn.commit()

xd = input('Enter user ID: ')
name = input('Enter user Name: ')
gender = input('Enter user Gender: ')
age = input('Enter user Age: ')
insertOrUpdate(xd, name, gender, age)

SN = 0

while True:
    ret, frame = cap.read()
    faces = faceDetect.detectMultiScale(frame, 1.3, 5)

    for (x, y, w, h) in faces:
        SN = SN + 1
        cv2.imwrite("DataSet/User." + str(xd) + "." + str(SN) + ".jpg", frame[y:y + h, x:x + w])
        cv2.rectangle(frame, (x-50, y-50), (x+ w+50, y+h+50), (255, 0, 0), 2)
        cv2.waitKey(100)

    cv2.imshow('Frame', frame)
    cv2.waitKey(1)
    if SN > 20:
        cap.release()
        cv2.destroyAllWindows()
        break

