import cv2
import numpy as np
from time import sleep
import time
from time import perf_counter

largura_min = 50  # Minimum rectangle width
altura_min = 50  # Minimum rectangle height

offset = 6  # Allowable error between pixel

pos_linha = 550  # Count line position

delay = 60  # Video FPS

detec = []
carros = 0

def pega_centro(x, y, w, h):
    x1 = int(w / 2)
    y1 = int(h / 2)
    cx = x + x1
    cy = y + y1
    return cx, cy


cap = cv2.VideoCapture('video.mp4')
subtracao = cv2.bgsegm.createBackgroundSubtractorMOG()

while True:
    ret, frame1 = cap.read()
    tempo = float(1 / delay)
    sleep(tempo)
    grey = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(grey, (3, 3), 5)
    img_sub = subtracao.apply(blur)
    dilat = cv2.dilate(img_sub, np.ones((5, 5)))
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    dilatada = cv2.morphologyEx(dilat, cv2.MORPH_CLOSE, kernel)
    dilatada = cv2.morphologyEx(dilatada, cv2.MORPH_CLOSE, kernel)
    contorno, h = cv2.findContours(dilatada, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cv2.line(frame1, (25, pos_linha), (1200, pos_linha), (255, 127, 0), 3)  #line length
    for (i, c) in enumerate(contorno):
        (x, y, w, h) = cv2.boundingRect(c)
        validar_contorno = (w >= largura_min) and (h >= altura_min)
        if not validar_contorno:
            continue

        cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
        centro = pega_centro(x, y, w, h)
        detec.append(centro)
        cv2.circle(frame1, centro, 5, (0, 0, 255), -1)

        for (x, y) in detec:
            if y < (pos_linha + offset) and y > (pos_linha - offset):
                carros += 1
                cv2.line(frame1, (25, pos_linha), (1200, pos_linha), (0, 127, 255), 3)
                detec.remove((x, y))
                #x = time.process_time()
                y = time.asctime()
                print("car is detected : " + str(carros))
                #print("To detect time : " + str(x))
                print("time : " + str(y))


    cv2.putText(frame1, "VEHICLE COUNT : " + str(carros), (450, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 5)
    cv2.imshow("Video Original", frame1)
    # cv2.imshow("Detectar",dilatada)

    if cv2.waitKey(1) == ord("m"):
        break
    x = int(perf_counter())
    if x == 10:
        print('For ' + str(x) +' second')
        y = carros
        print('Car count is: ' + str(y))


cv2.destroyAllWindows()
cap.release()


