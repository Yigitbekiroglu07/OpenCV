import cv2 as cv #OpenCV kütüphanesi cv ile çağrılır.
import numpy as np

path="opencv.png" # resmin yolu(adresi)

img = cv.imread(path) #resmi oku
cv.namedWindow("colored", cv.WINDOW_AUTOSIZE) # kendin isim ver, resmin boyutunu koru
cv.imshow("colored", img )
cv.waitKey(1) # 0 girlirse sonusza kadar bellekte yer tutar demek.

m1 = np.copy(img) #resmin kopyası alınır
m2=img

type(img)

img[100:200,200:300, :] = 0 # 0 >> siyah, 255 >> beyaz
cv.imshow("m2",m2)
cv.waitKey(0)

m3= np.zeros(img.shape, img.dtype) #resmin booyutunda ve tipinde 0'lar oluşturulur.
cv.imshow("m3",m3)
cv.waitKey(0)

m4=np.zeros([512,512], np.uint8) #resmin booyutundan farklı görsel oluşturma
cv.imshow("m4",m4)
cv.waitKey(0)

img = np.ones((550,720,3))
black = (0,0,0) #Tuple
red=(0,0,255) #Tuple
green = (0,255,0) #Tuple

cv.rectangle(img,(480,250),(100,450),black,8) #Dikdörtgen oluşturmak için
cv.rectangle(img,(580,150),(200,350),black,8)
cv.line(img, (100,450),(200,350),black,8) #Çizgi oluşturmak için
cv.line(img, (480,250),(580,150),black,8)
cv.line(img, (100,250),(200,150),black,8)
cv.line(img, (480,450),(580,350),black,8)

#Yazı yazılacak nokta
start_point = (150,100) #Başlangıç noktası
font_thickness = 2 #kalınlığı
font_size = 1 #boyutu
font = cv.FONT_HERSHEY_TRIPLEX #font
#Resmi göstermek için
cv.putText(img,"kendicizer.com",start_point,font,font_size,black,font_thickness)
cv.imshow('dikdortgen',img)
cv.waitKey(0)