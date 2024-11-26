import cv2 as cv
import numpy as np

image = np.zeros((512,512,3),dtype=np.uint8) # 512'ye 512 (boyut) üç kanallı sıfırlar oluşturuldu
cv.rectangle(image,(100,100),(300,300),(255,0,0),2,cv.LINE_8,0) #kare oluşturuldu
cv.circle(image,(256,256),50,(0,0,255),2,cv.LINE_8,0) #daire oluşturuldu
cv.ellipse(image,(256,256),(150,150),360,0,360,(0,255,0),2,cv.LINE_8,0) #elips oluşturuldu
cv.imshow("img",image)
cv.waitKey(0)