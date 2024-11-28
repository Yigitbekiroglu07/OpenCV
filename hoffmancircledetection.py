#Amaç daire saptamak
import cv2 as cv
import numpy as np

# Resmi yükle
path = "coins.jpg"
src = cv.imread(path)
if src is None:
    print("Resim yüklenemedi. Dosya yolunu kontrol edin!")
    exit()

# Gri tonlama ve bulanıklaştırma
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
gray = cv.GaussianBlur(gray, (9, 9), 2, 2)  # Gürültü giderme

# HoughCircles ile daire algılama
circles = cv.HoughCircles(
    gray,
    cv.HOUGH_GRADIENT,
    dp=1,
    minDist=10,
    param1=100,
    param2=50,
    minRadius=20,
    maxRadius=100,
)

# 1. Parametre = Resim, 2.Parametre Hoffman yöntemindeki opsiyon, 3.parametre = resmin çözünürlüğü
# 4. Parametre = Saptanmış olan dairenin merkeziyle min uzaklık, 5.Parametre = Kenar saptama, 6.Parametre = daireleri saptama
# 7. Parametre = minimum yarıçap, 8.Parametre = maksimum yarıçap

if circles is not None:
    circles = np.round(circles[0, :]).astype("int")  # Daire parametrelerini tam sayıya çevir
    for c in circles:
        cx, cy, r = c
        print(f"Daire Merkezi: ({cx}, {cy}), Yarıçap: {r}")
        # Daire merkezi işaretleme
        cv.circle(src, (cx, cy), 2, (0, 255, 0), 2, 8, 0)
        # Daire çizme
        cv.circle(src, (cx, cy), r, (0, 0, 255), 2, 8, 0)

# Sonuçları göster
cv.imshow("Hough Circle Detection", src)
cv.waitKey(0)
cv.destroyAllWindows()

