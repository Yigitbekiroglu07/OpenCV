import cv2 as cv #OpenCV kütüphanesi cv ile çağrılır.
import numpy as np

path1="sol.jpg" # resmin yolu(adresi)
path2="sag.jpg" # resmin yolu(adresi)

img1=cv.imread(path1)
img2=cv.imread(path2)

cv.imshow("sol",img1)
cv.waitKey(0)

cv.imshow("sag",img2)
cv.waitKey(0)

#Resimleri birleştirmek için
horizontal=np.hstack((img2,img1)) 
cv.imshow("tam",horizontal)
cv.waitKey(0)
cv.destroyAllWindows()