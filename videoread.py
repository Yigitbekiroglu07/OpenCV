import cv2 as cv
import numpy as np

capture = cv.VideoCapture("akdeniz.mp4")
height = capture.get(cv.CAP_PROP_FRAME_HEIGHT)#Videonun yüksekliği
width = capture.get(cv.CAP_PROP_FRAME_WIDTH)#Videonun genişliği
count = capture.get(cv.CAP_PROP_FRAME_COUNT)
fps = capture.get(cv.CAP_PROP_FPS)#Videonun fps değeri
print(height,width,count,fps)

    