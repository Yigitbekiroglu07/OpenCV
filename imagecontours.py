# Contur: Bir rengin veya yoğunluğunun sahip olduğu tüm sürekli noktaları birleştiren kapalı bir eğridir.
# Conturlar bir görüntüde bulunan nesnelerin şekillerini temsil eder. Geçiş noktalarını tespit ederiz.
import cv2 as cv

def threshold_demo(image):
    dst = cv.GaussianBlur(image, (3,3),0) #Gürültüyü azaltır kenarları koruyup görüntüyü yumuşatır.
    gray = cv.cvtColor(dst,cv.COLOR_BGR2GRAY)
    ret,binary = cv.threshold(gray,0,255,cv.THRESH_OTSU | cv.THRESH_BINARY)
    cv.imshow("binary", binary)
    return binary
def canny_demo(image): # Kenar bulmak için
    t = 100
    canny_output = cv.Canny(image, t, t*2)
    cv.imshow("canny_output", canny_output)
    return canny_output

src = cv.imread("anadearmas.jpg")
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src)
cv.waitKey(1)

binary = threshold_demo(src) #Görünütünün binary hale gelmesi
canny = canny_demo(src) 
contours, hierarchy = cv.findContours(canny, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

for c in range(len(contours)):
    cv.drawContours(src, contours, c, (0, 0, 255), 2, 8)

cv.imshow("contours-demo", src)
cv.waitKey(0)
