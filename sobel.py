# Sobel --> Kenarları algılamak = renk geçişlerini anlamak
# Sobel: Bir görüntüden türevlerini hesaplamak.
import cv2 as cv

src = cv.imread("opencvr.png")

h, w = src.shape[:2]  # Resmin boyutlarını al

# Sobel gradyanlarını hesapla (X ve Y eksenlerinde)
x_grad = cv.Sobel(src, cv.CV_32F, 1, 0)  # X yönünde türev
y_grad = cv.Sobel(src, cv.CV_32F, 0, 1)  # Y yönünde türev

# Gradyanları mutlak değerlere dönüştür
x_grad = cv.convertScaleAbs(x_grad)
y_grad = cv.convertScaleAbs(y_grad)

# X gradyanını göster
cv.imshow("x_grad", x_grad)
cv.waitKey(0)

# Y gradyanını göster
cv.imshow("y_grad", y_grad)
cv.waitKey(0)

# X ve Y gradyanlarını birleştir
dst = cv.add(x_grad, y_grad, dtype=cv.CV_16S)
dst = cv.convertScaleAbs(dst)

# Sonuç gradyanı göster
cv.imshow("gradient", dst)
cv.waitKey(0)
