# Canny --> Kenar tespiti için kullanılır
# Piksellerin renk farklılaşmasından yararlanılır.
import cv2 as cv

src = cv.imread("ataturk.jpg")
cv.imshow("ataturk",src)
cv.waitKey(0)

edge = cv.Canny(src,100,200) # Kuvvetli kenarları bulmak için 2. ve 3. argüman değerleri büyük seçilir.
cv.imshow("mask image",edge)
cv.waitKey(0)