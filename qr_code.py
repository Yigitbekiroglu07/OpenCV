# QR Code: Toyota'nın yan kuruluşu tarafından gerçekleştirilmiş 2D barkod sistemidir. (1uick response)
# Barkodlar sadece yatay yönlü bilgi tutar, QR Kodları ise hem yatay hem dikey yönlü bilgi tutar.
import cv2 as cv
import numpy as np

path = "qrcode.png"
src = cv.imread(path)
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
qrcoder = cv.QRCodeDetector() # QR kodunun köşelerinin çıktı dizisini verir, QR kodu üzerinden çözülen metni düzeltilmiş ikili çıktıyı verir.
codeinfo, points, straight_qrcode = qrcoder.detectAndDecode(gray)
print(points)

result = np.copy(src) # kaynak resmin kopyası

cv.drawContours(result, [np.int32(points)],0,(0,0,255),2) #Contour, sınırı boyunca aynı yoğunluğa sahip tüm noktaları birleştiren bir çizgi
# 1.Paramete --> ilgili resmi ifade eder
# 2.Parametre --> Contours argümanı
# 3.Parametre --> Çizilecek Contours'u gösterecek parametre
# 4.Parametre --> Contours renk bilgisini temsil eder.
# 5.Parametre --> Contours kalınlığını verir.

print("qrcode information is :\n%s" % codeinfo ) #QR Code üzerinden çözülecek metin

cv.imshow("result", result)
cv.waitKey(0)