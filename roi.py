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
cv.waitKey(0)

img[0:450, 0:350, :] = roi #Ana resmin 0:450, 0:350 koordinatlarına roi'yi ata.
cv.imshow("img",img)
cv.waitKey(0)

res= cv.resize(roi,None,fx=0.4,fy=0.4,interpolation=cv.INTER_CUBIC) #orijinal resme eklenen roi bölgesini küçültme işlemi
cv.imshow("res",res)
cv.waitKey(0)

res.shape[:2] #Yeni oluşturulan resmin boyutu

img[0:135, 0:105, :] = res 
cv.imshow("img",img)
cv.waitKey(0)

src[0:135, 0:105, :] = res #Son düzeltilen hal orijinal hale eklenir
cv.imshow("img",src)
cv.waitKey(0)