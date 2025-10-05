import cv2

cap = cv2.VideoCapture(0)
faceDetect = cv2.CascadeClassifier('haarcascade_frontalface.xml')

id = input('Enter your ID:')
SN = 0

while True:
    ret, frame = cap.read()
    faces = faceDetect.detectMultiScale(frame, 1.3, 5)

    for (x, y, w, h) in faces:
        SN = SN + 1
        cv2.imwrite("DataSet/user." + str(id) + "." + str(SN) + ".jpg", frame[y:y + h, x:x + w])
        cv2.rectangle(frame, (x-50, y-50), (x+ w+50, y+h+50), (255, 0, 0), 2)
        cv2.waitKey(100)

    cv2.imshow('Frame', frame)
    cv2.waitKey(1)
    if SN > 20:
        cap.release()
        cv2.destroyAllWindows()
        break