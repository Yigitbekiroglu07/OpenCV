import cv2 as cv
import numpy as np

path = "opencvr.png"
src = cv.imread(path,cv.IMREAD_GRAYSCALE)
#MinMaxLoc
min_value, max_value, min_loc, max_loc = cv.minMaxLoc(src)
print("min value: %.2f, max value: %.2f" %(min_value,max_value)) #piksellerin min ve max değerleri
print("min loc:",min_loc,",""max loc:",max_loc) #piksellerin min ve max değerlerinin lokasyonları

#meanStddev
means, stddev = cv.meanStdDev(src) #Ortalama ve standart sapma belirleme

src[np.where(src<means)]=0 #mean'den küçük olan değerlere 0 ataması yap.
src[np.where(src>means)]=255 #mean'den küçük olan değerlere 255 ataması yap.
cv.imshow("binary",src)
cv.waitKey(0)