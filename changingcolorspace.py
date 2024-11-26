import cv2 as cv
#RGB Form
path="opencvr.png" # resmin yolu(adresi)
img = cv.imread(path) #ilgili resmin dizinini ver, resmi okur
cv.namedWindow("img", cv.WINDOW_AUTOSIZE) # kendin isim ver, resmin boyutunu koru
cv.imshow("rgb",img)
cv.waitKey(0)
#Gray Form
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY) #Resmi griye çevirir.
cv.imshow("gray",gray)
cv.waitKey(0)
#HSV --> RGB gibi bir renk uzayı -- Nesnelerin takibini kolaylaştırır. H=Rengin özü, S=Saturation, V=Value
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV) #resmi HSV'ye çevirir.
cv.imshow("hsv",hsv)
cv.waitKey(0)