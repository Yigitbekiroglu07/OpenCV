import cv2 as cv
path = "MIUI.jpg"
src = cv.imread(path)

#Roi --> Resmin sadece belirli bölgesine odaklanmak --> Performans kazandırır.

h,w = src.shape[:2] #Boyut bilgileri tutulur.
img = src.copy() #Resmin kopyası

#Roi bölgesini seçme
roi = img[300:750, 950:1300, :] #resmin belli bölümünü seçme
roi.shape[:2] #ilgili satır sütün bilgisini verir.
cv.imshow("roi",roi)
cv.waitKey(1)

img[0:450, 0:350, :] = roi #Ana resme roi'yi ekle
cv.imshow("img",img)
cv.waitKey(1)

res= cv.resize(roi,None,fx=0.4,fy=0.4,interpolation=cv.INTER_CUBIC) #orijinal resme eklenen roi bölgesini küçültme işlemi
cv.imshow("res",res)
cv.waitKey(1)

res.shape[:2] #Yeni oluşturulan resmin boyutu

src[0:135, 0:105, :] = res #Son düxeltilen hal orijinal hale eklenir
cv.imshow("img",img)
cv.waitKey(1)

src[0:135, 0:105, :] = res #Son düxeltilen hal orijinal hale eklenir
cv.imshow("img",src)
cv.waitKey(0)