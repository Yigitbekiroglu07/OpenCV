# Bileteral Filter: Resmin kenarlarını koruyarak görüntüyü yumuşatma = Gürültüyü azaltma - Blurlama yapar. Çift taraflı filtreleme yapar.
# Gürültü: Resimdeki gereksiz detaylar
import cv2 as cv
import numpy as np
# Resmi getirme
src = cv.imread("cry.jpg")
cv.namedWindow("input",cv.WINDOW_AUTOSIZE)
cv.imshow("input",src)
cv.waitKey(1)

h,w = src.shape[:2] #Resmin boyut bilgisi

dst = cv.bilateralFilter(src,0,80,10) # 2.argüman = çap bilgisi, 3.argüman= renklerin karışması, 4.argüman = piksellerin karışması

result = np.zeros([h,w*2,3],dtype=src.dtype) # 0'lardan oluşan array
result[0:h,0:w,:] = src # result'ın bir bölümünw resmin ilk hali konur.
result[0:h,w:2*w,:] = dst # result'un diğer bölümüne dönüştürülmüş hali konur.

cv.imshow("result",result)
cv.waitKey(0)
