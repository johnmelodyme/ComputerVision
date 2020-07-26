import cv2
import os
from keras.models import load_model
import numpy as np
from pygame import mixer
import time

mixer.init()
mixer.music.load("assets/alarm.mp3")

face = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt.xml')
leye = cv2.CascadeClassifier('cascades/data/haarcascade_lefteye_2splits.xml')
reye = cv2.CascadeClassifier('cascades/data/haarcascade_righteye_2splits.xml')

lbl=['Close','Open']

