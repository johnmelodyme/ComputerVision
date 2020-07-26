#!/usr/bin/env python
Copyright = """
                  Copyright 2020 © John Melody Me

      Licensed under the Apache License, Version 2.0 (the "License");
      you may not use this file except in compliance with the License.
      You may obtain a copy of the License at

                  http://www.apache.org/licenses/LICENSE-2.0

      Unless required by applicable law or agreed to in writing, software
      distributed under the License is distributed on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
      See the License for the specific language governing permissions and
      limitations under the License.
      @Author : John Melody Me
      @Copyright: John Melody Me & Tan Sin Dee © Copyright 2020
      @INPIREDBYGF: Cindy Tan Sin Dee <3
"""
import cv2
import time
import pandas
from datetime import datetime

print(Copyright)
STATIC_BACK = None
MOTION_LIST = [None, None]
TIME = []


df = pandas.DataFrame(columns= ["Start", "End"] )
video = cv2.VideoCapture(0)
while True:
      check, frame = video.read()
      motion = 0
      grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
      grey = cv2.GaussianBlur(grey, (21,21), 0)
      if STATIC_BACK is None:
            STATIC_BACK = grey
            continue
      differentFrame = cv2.absdiff(STATIC_BACK, grey)
      thresholdFrame = cv2.threshold(differentFrame, 30, 255, cv2.THRESH_BINARY) [1]
      thresholdFrame = cv2.dilate(thresholdFrame, None, iterations = 2)
      (cnts, hierarchy) = cv2.findContours(thresholdFrame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
      for contour in cnts:
            if cv2.contourArea(contour) < 10000 :
                  continue
            motion = 1
            (x, y, w, h) = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
      MOTION_LIST.append(motion)
      MOTION_LIST = MOTION_LIST[-2:]
      if MOTION_LIST [-1] == 1 and MOTION_LIST[-2] == 0:
            TIME.append(datetime.now())
      if MOTION_LIST [-1] == 0 and MOTION_LIST[-2] == 1:
            TIME.append(datetime.now())
      cv2.imshow("GREY FRAME", grey)
      cv2.imshow("DIFFERENCE FRAME", differentFrame)
      cv2.imshow("THRESHOLD FRAME", thresholdFrame)
      cv2.imshow("COLOUR FRAME", frame)
      key = cv2.waitKey(1)
      if key == ord("q"):
            if motion == 1:
                  print("q", "pressed")
                  TIME.append(datetime.now())
            break
for i in range(0, len(time), 2):
      df = df.append({"START":TIME[i], "END":TIME[i + 1]}, ignore_index = True)
TODAY = datetime.today
df.to_csv("motionDetected.csv")
video.release()
cv2.destroyAllWindows()