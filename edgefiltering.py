import numpy as np
import cv2 as cv

# EdgeFiltering: Kenarları koruyarak filtreleme işlemi gerçekleştirme

src = cv.imread("cry.jpg")
cv.imshow("input", src)
cv.waitKey(0)

# Resmin boyutlarını al
h, w = src.shape[:2]

# Edge Preserving Filter (Kenar Koruyucu Filtre) uygula
dst = cv.edgePreservingFilter(src, sigma_s=10, sigma_r=0.9, flags=cv.RECURS_FILTER) #sigma_s --> 0-200 arası, sigma_r --> 0-1 arası değer alır.
#sigma_s --> Blurluğu ifade eder.
#sigma_r --> ana odak dışındaki kenarların ne kadar dikkate alınıp alınmayacağını ifade eder. 

# Sonuçları birleştirmek için bir boş resim oluştur
result = np.zeros((h, w * 2, 3), dtype=src.dtype)
result[0:h, 0:w, :] = src          # Orijinal resmi sola koy
result[0:h, w:2 * w, :] = dst      # Filtrelenmiş resmi sağa koy

# Birleştirilen resmi boyutlandır --> Küçült
result = cv.resize(result, (w, h // 2)) # Resim boyutu küçültme fonksiyonu
cv.imshow("result",result)
cv.waitKey(0)
