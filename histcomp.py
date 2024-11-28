import cv2 as cv

src1 = cv.imread("MIUI.jpg")
src2 = cv.imread("work.jpg")
src3 = cv.imread("orman.jpg")
# Neden HSV --> Resimlerde renkleri ayırma konusunda imkan sağlar.
hsv1 = cv.cvtColor(src1,cv.COLOR_BGR2HSV)
hsv2 = cv.cvtColor(src2,cv.COLOR_BGR2HSV)
hsv3 = cv.cvtColor(src3,cv.COLOR_BGR2HSV)

# calcHist
# ([hsv1], [0, 1], None, [60, 64], [0, 180, 0, 256]) --> 1. Argüman: Resimler, 2.Argüman: Histogramı hesaplayacak kanallar, 4.Argüman: Histogram boyutları 5.Argüman:Aralıklar
hist1 = cv.calcHist([hsv1], [0, 1], None, [60, 64], [0, 180, 0, 256])
hist2 = cv.calcHist([hsv2], [0, 1], None, [60, 64], [0, 180, 0, 256])
hist3 = cv.calcHist([hsv3], [0, 1], None, [60, 64], [0, 180, 0, 256])


# normalize --> Belirli bir görseldeki piksellerin yoğunluk değerlerini değiştirip görüntüyü normalleştirmek. Kontsrat arttırlır.
cv.normalize(hist1, hist1, 0, 1.0, cv.NORM_MINMAX)
cv.normalize(hist2, hist2, 0, 1.0, cv.NORM_MINMAX)
cv.normalize(hist3, hist3, 0, 1.0, cv.NORM_MINMAX)

# compareHist --> Histogram karşılaştırma
# HISTCMP_CORREL --> 0 ile 1 arasında benzerlik gösterir.
cv.compareHist(hist1, hist2, cv.HISTCMP_CORREL)
cv.compareHist(hist1, hist3, cv.HISTCMP_CORREL)
cv.compareHist(hist2, hist3, cv.HISTCMP_CORREL)
