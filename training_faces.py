#!/usr/bin/env python
#
#              Copyright 2020 © John Melody Me
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#             http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# @Author : John Melody Me
# @Copyright: John Melody Me & Tan Sin Dee © Copyright 2020
# @INPIREDBYGF: Cindy Tan Sin Dee <3
# @Project: FacialRecognition.py
import cv2
import os as Machine
from PIL import Image
import numpy as np
import pickle

faces_cascades = cv2.CascadeClassifier("cascades/data/haarcascade_frontalface_alt2.xml")
BASE_DIRECTORY = Machine.path.dirname(Machine.path.abspath(__file__))
IMAGE_DATABASE_DIRECTORY = Machine.path.join(BASE_DIRECTORY, "model")
# print(IMAGE_DATABASE_DIRECTORY)
# Recognizer :
recognizer = cv2.face.LBPHFaceRecognizer_create() #pip3 install opencv-contrib-python --user
CURRENT_IDENTICATION = 0
LABEL_ID = {}
y_labels = []
x_train = []

for root, dirs, files in Machine.walk(IMAGE_DATABASE_DIRECTORY):
      for file in files:
            if file.endswith("jpg") or file.endswith("png"): # Prefered (.png)
                  path = Machine.path.join(root, file)
                  label = Machine.path.basename(Machine.path.dirname(path)).replace(" ","-").upper()
                  print(label, path)
                  if label in LABEL_ID:
                        pass
                  else:
                        LABEL_ID[label] = CURRENT_IDENTICATION
                        CURRENT_IDENTICATION += 1
                  id_ = LABEL_ID[label]
                  print(LABEL_ID)
                  # y_labels.append(label)
                  # x_train.append(path) # Very this and Convert into numpy array, Grey
                  pil_image = Image.open(path).convert("L") # greyscaled
                  #Resizing:
                  # size = (550, 550)
                  # final_img = pil_image.resize(size, Image.ANTIALIAS)
                  image_array = np.array(pil_image, "uint8")
                  print(image_array)
                  face = faces_cascades.detectMultiScale(image_array, scaleFactor=1.5, minNeighbors=5)
                  for (x, y, w, h) in face:
                        ROI = image_array[y:y+h, x:x+w]
                        x_train.append(ROI)
                        y_labels.append(id_)
            else :
                  error = "No Model"
                  print(error)
print(y_labels)
print(x_train)

with open("labels.pickle", "wb") as file:
      pickle.dump(LABEL_ID, file)
recognizer.train(x_train, np.array(y_labels))
recognizer.save("training.yml")
print(recognizer)