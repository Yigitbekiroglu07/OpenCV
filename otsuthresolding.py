# otsuthresolding: Otomatik görüntü eşikleme yapma. Giriş görüntüsünü ikili görüntüye çevirir.
# İkili (binary) görüntü: Görüntünün siyah - beyaz olarak tanımlanması. Amaç gürültüyü azaltma.
# grayscale'den farkı burada gri renk olmaz belli thresold'un altında kalanlar siyah, üstündekiler beyazdır.
import cv2 as cv
import numpy as np

# Resmi yükle ve göster
src = cv.imread("anadearmas.jpg")
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src)
cv.waitKey(0)

# Resmi gri tona çevir
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

# Otsu eşikleme uygula
ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU) # Binary eşitleme ve otsu methoduyla

# Resim boyutlarını al
h, w = src.shape[:2]

# Eşiklenmiş görüntüyü göster
cv.imshow("binary", binary)
cv.waitKey(0)
