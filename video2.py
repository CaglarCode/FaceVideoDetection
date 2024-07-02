import pygame
import cv2
import numpy as np
import time

# Pygame ses ayarları
pygame.mixer.init()
sound = pygame.mixer.Sound("/Users/caglartogan/Downloads/siren.mp3")

# Yüz tanıma için Haar Cascade dosyası
face_cascade = cv2.CascadeClassifier('/Users/caglartogan/Downloads/haarcascade_frontalface_default.xml')

# Kamerayı açın .Benim bilgisayarimda 1 eger 0 yaparsam telefonun kamerasini aciyor
cap = cv2.VideoCapture(1)  # Dahili kamerayı kullan
if not cap.isOpened():
    print("Kamera acilamadi")
    exit()

is_drinking = False

while True:
    ret, frame = cap.read()
    if not ret:
        print("Kamera görüntüsü alinamadi")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    if len(faces) == 0:
        is_drinking = False
        print("Yüz algılanamadı")
    else:
        for (x, y, w, h) in faces:
            mouth_roi = gray[y:y+h, x:x+w]
            _, thresh = cv2.threshold(mouth_roi, 100, 255, cv2.THRESH_BINARY)
            white_pixels = np.sum(thresh == 255)

            if white_pixels > 10000:
                if not is_drinking:
                    sound.play()
                    is_drinking = True
            else:
                is_drinking = False

            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    if not is_drinking:
        pygame.mixer.stop()

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
