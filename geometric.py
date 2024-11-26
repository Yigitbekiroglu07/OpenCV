import cv2 as cv
import numpy as np
path = "work.jpg"
img = cv.imread(path)

#Shape --> satır - sütun bilgisi verir
rows = img.shape[0] #Satır Bilgisi
cols = img.shape[1] #Sütun Bilgisi
print(rows,cols)

#Kaydırma İşlemi
M = np.float32([[1,0,300],[0,1,90]]) #Çıktıya ait koordinat bilgileri
shifted = cv.warpAffine(img,M,(cols,rows)) #Affine methodu, kaynak resmi belirtilen matrise çevirir.

cv.imshow("original",img)
cv.waitKey(0)

cv.imshow("shifted",shifted)
cv.waitKey(0)

#Döndürme İşlemi
M= cv.getRotationMatrix2D((cols/2, rows/2),90,1) #Döndürme için kullanılan fonk.
rotation = cv.warpAffine(img,M,(cols,rows)) #Affine methodu, kaynak resmi belirtilen matrise çevirir.
cv.imshow("rotation",rotation)
cv.waitKey(0)

#Scaling --> Resim boyutu ayarlama - Yeniden Boyutlandırma
res= cv.resize(img,None,fx=0.4,fy=0.4,interpolation=cv.INTER_CUBIC) #Resmin boyutunu ayarlayan fonk. fx ve fy'dan 1'den küçük olmalı ki şekil küçülsün.
cv.imshow("res",res)
cv.waitKey(0)

cv.destroyAllWindows() #tüm pencereleri kapa