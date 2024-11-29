# Görüntü keskinleştirme --> Temel amaç daha keskin hatlara sahip, daha düşük kalitede görüntü elde etmek
import cv2 as cv
import numpy as np
path = "cry.jpg"
src = cv.imread(path)

sharpen_op = np.array([[0,-1,0], [-1,5,-1], [0,-1,0]], dtype=float) # Görüntünün bir araya gelmesini istediğimiz 2D matris

sharpen_image = cv.filter2D(src, cv.CV_32F, sharpen_op) #Görüntüye filtre uygulanmak istendiğinde o görüntüyü dönüştürülecek matrisle bir araya getirmek için kullanılır

sharpen_image = cv.convertScaleAbs(sharpen_image) # Ölçekleme, mutlak değer alma, işaretsiz 8 bite dönüştürme işlemi yapar.

#Resmi göster
cv.imshow("sharpen_image", sharpen_image)
cv.waitKey(0)