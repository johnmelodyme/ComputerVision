#!/usr/bin/env python
# John Melody Me
import cv2
from datetime import datetime, date
import numpy as np
import pickle
import random


labels = {"Person_Name": 1}
faces_cascades = cv2.CascadeClassifier("cascades/data/haarcascade_frontalface_alt2.xml")
# Recognizer :
recognizer = cv2.face.LBPHFaceRecognizer_create() #pip3 install opencv-contrib-python --user
recognizer.read("training.yml")
with open("labels.pickle", "rb") as file:
      old_labels = pickle.load(file)
      labels = {v:k for k, v in old_labels.items()}
# CV2 Config:
capture = cv2.VideoCapture(0)
# print(capture)
# print(capture.read())
title = "Facial Recognition"
#Capture Frame by Frame
while (True):
      ret, frame = capture.read()
      #Covert cascades to GREY:
      grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
      faces = faces_cascades.detectMultiScale(grey, scaleFactor=1.5, minNeighbors=5)
      for (x, y, w, h) in faces:
            # print(x, y, w, h)
            REGION_OF_INTEREST_GREY = grey[y:y+h, x:x+w] # Location Of the Face for Grey
            REGION_OF_INTEREST_COLOURED = frame[y:y+h, x:x+w] # Location Of the Face for Coloured
            # Prediction:
            id_ , conf = recognizer.predict(REGION_OF_INTEREST_GREY)
            if conf >= 45 and conf <= 85:
                  # print(id_)
                  print("Detected identity" ,labels[id_], "Accuracy: ", random.random())
                  # OPENCV PUT TEXT:
                  font = cv2.FONT_HERSHEY_COMPLEX
                  name = labels[id_]
                  COLOUR = (255, 255, 255)
                  stroke = 2
                  cv2.putText(frame, name, (x, y), font, 1, COLOUR, stroke, cv2.LINE_AA)
            img_item = "exported_data/face.png"
            cv2.imwrite(img_item, REGION_OF_INTEREST_GREY)
            Colour = (255, 0, 0)
            Stroke = 2
            END_CORD_X = x + w
            END_CORD_Y = y + h
            cv2.rectangle(frame, (x, y), (END_CORD_X, END_CORD_Y), Colour, Stroke)
      #Display Result Frame:
      cv2.imshow(title, frame)
      if cv2.waitKey(20) & 0xFF == ord("q"):
            break
# When Everything's done, Release:
capture.Release()
cv2.destroyAllWindows()