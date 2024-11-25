#Normalizasyon bellekte daha az yer tutmayı sağlar. 0 ve 255 yerine 0 ve 1
#Diğer normalizasyon yöntemleri --> NORM_INF, NORML1, NORML2

import cv2 as cv
import numpy as np

path = "opencvr.png"
src = cv.imread(path)
print(src.shape)#resmin boyutunu alma

#Resmi griye çevirme
gray = cv.cvtColor(src,cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)
cv.waitKey(0)
print(gray.shape)
print(gray)

gray=np.float32(gray)
print(gray)

#NormalizasyonMinMax --> Verilen 2 değer arasında dönüştürme yapar.
min_value, max_value, min_loc, max_loc = cv.minMaxLoc(gray)
print("min value: %.2f, max value: %.2f" % (min_value,max_value)) #piksellerin min ve max değerleri

means, stddev = cv.meanStdDev(gray) #Ortalama ve standart sapma belirleme
print("mean: %.2f, stddev: %.2f" % (means,stddev))

dst = np.zeros(gray.shape,dtype=np.float32) # 0'lardan oluşan bir çıktı arrayi

cv.normalize(gray,dst=dst,alpha=0,beta=1.0,norm_type=cv.NORM_MINMAX) # 0 ile 1 arası dönüştürme işlemi
print(dst)

cv.imshow("NORM_MINMAX",dst)
cv.waitKey(0)

print("min value: %.2f, max value: %.2f" % (min_value,max_value)) #piksellerin min ve max değerleri

means, stddev = cv.meanStdDev(dst) #Ortalama ve standart sapma belirleme
print("mean: %.2f, stddev: %.2f" % (means,stddev))