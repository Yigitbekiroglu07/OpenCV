import cv2 as cv #OpenCV kütüphanesi cv ile çağrılır.

path="opencv.png" # resmin yolu(adresi)

img = cv.imread(path) #resmi oku

cv.namedWindow("colored", cv.WINDOW_AUTOSIZE) # kendin isim ver, resmin boyutunu koru

cv.imshow("colored", img )

cv.waitKey(1000) # 0 girlirse sonusza kadar bellekte yer tutar demek.

#cvtColor

gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY ) # Resmi gri yapar.
cv.imshow("gray", gray)
cv.waitKey(1000)

#imwrite --> kaydetme işlemi yapar

cv.imwrite(path,gray)

cv.destroyAllWindows()

# Orijinal görüntü göstermeden direkt siyah-beyaz yapma

img = cv.imread(path, cv.imread_GRAYSCALE) # path yanına siyah-beyaz yapmak için kod eklendi
cv.namedWindow("gray", cv.WINDOW_AUTOSIZE) # kendin isim ver, resmin boyutunu koru
cv.imshow("gray", img ) #Resmi göster
cv.waitKey(2000)