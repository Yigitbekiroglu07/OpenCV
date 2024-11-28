# Görüntü Segmentasyonu --> Börüntünün belirli bir bölümünü alma
import cv2 as cv
import numpy as np

src = cv.imread("anadearmas.jpg")
src = cv.resize(src, (0, 0), fx=0.5, fy=0.5) #Resmin boyutunu küçültme
r = cv.selectROI('input', src, False) # İlgilenilen alanı seçme = ROI

roi = src[int(r[1]):int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])] #ROI alanı belirlenir
img = src.copy() #Resmin kopyası oluşturulur.

cv.rectangle(img, (int(r[0]), int(r[1])), 
             (int(r[0]) + int(r[2]), int(r[1]) + int(r[3])),
             (255, 0, 0), 2) #Çizim İşlemi

mask = np.zeros(src.shape[:2], dtype=np.uint8) #Mask işlemi yapılır
#Numpy arrayleri oluşturma
rect = (int(r[0]), int(r[1]), int(r[2]), int(r[3]))

bgdmodel = np.zeros((1, 65), np.float64)
fgdmodel = np.zeros((1, 65), np.float64)
# Belirlenen bölgenin arka plandan ayrıştırılması ve öne çıkarılması işlemi
cv.grabCut(src, mask, rect, bgdmodel, fgdmodel, 11, mode=cv.GC_INIT_WITH_RECT)
# Olası ön plan bölgelerini ayırma
mask2 = np.where((mask == 1) + (mask == 3), 255, 0).astype('uint8')
# Bitwise methodu, bit düzeyinde birleşme imkanı sağlar.
result = cv.bitwise_and(src,src,mask=mask2)

cv.imshow("roi",roi) # son hal
cv.imshow("result",result)
cv.waitKey(0)
