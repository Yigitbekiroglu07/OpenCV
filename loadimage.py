import cv2 as cv #OpenCV kütüphanesi cv ile çağrılır.

path="flag.jpg" # resmin yolu(adresi)

img = cv.imread(path) #ilgili resmin dizinini ver, resmi okur

#type(img)

#namedWindows >> Resimleri tutmak için pencere oluşturur.
cv.namedWindow("openCV_test", cv.WINDOW_AUTOSIZE) #cv.WINDOW_AUTOSIZE, resmi orijinal boyutuyla görmemizi sağlar.

#imshow --> resmi gösterir
cv.imshow("openCV_test", img )

cv.waitKey(1000) # 0 girlirse sonusza kadar bellekte yer tutar demek.

cv.destroyAllWindows() #Tüm pencereler kapatılır.