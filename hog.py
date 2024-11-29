# HOG --> Yayaları belirlemede kullanılan yöntem
import cv2 as cv

src = cv.imread("pedestrian.jpg")

hog = cv.HOGDescriptor() # Sınıflandırıcı yöntemi

hog.setSVMDetector(cv.HOGDescriptor_getDefaultPeopleDetector()) #İlgili parametreleri Hog yöntemi için göstermiş oluruz

rects, weights = hog.detectMultiScale(src, winStride=(4,4), padding=(8,8),scale=(1.25))
# winStride: Pencere adımı
# scale: Pencere artışı katsayısı

for(x,y,w,h) in rects:
    cv.rectangle(src,(x,y),(x+w,y+h),(0,255,0),2)
    
cv.imshow("hog", src)
cv.waitKey(0)