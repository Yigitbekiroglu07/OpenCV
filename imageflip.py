import cv2 as cv #OpenCV kütüphanesi cv ile çağrılır.

path="opencvr.png" # resmin yolu(adresi)
img = cv.imread(path) #ilgili resmin dizinini ver, resmi okur

#X Flip --> X ekseninde kaydırma
dst1=cv.flip(img,0)
cv.imshow("x",dst1)
cv.waitKey(0)

#Y Flip --> Y ekseninde kaydırma
dst2=cv.flip(img,1)
cv.imshow("y",dst2)
cv.waitKey(0)

#XY Flip --> XY ekseninde kaydırma
dst3=cv.flip(img,-1)
cv.imshow("XY",dst3)
cv.waitKey(0)

