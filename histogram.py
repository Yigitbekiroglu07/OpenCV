import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
# Histogram --> Sayısal değişkenlerin dağılımını göstermek için kullanılan grafik yöntem
# Örneğin --> 0-10 yaş arasında 5 kişi var, 10-20 yaş arasında 10 kişi var gibi.
def custom_hist(gray): #Gri resimleri göstermek için kullanılır
    h, w = gray.shape #Görselin boyut bilgileri alınır
    hist = np.zeros([256], dtype=np.int32) # 0'dan 256'ya kadar boş değer oluşturuldu
    for row in range(h):
        for col in range(w):
            pv = gray[row, col]
            hist[pv] += 1

    y_pos = np.arange(0, 256, 1, dtype=np.int32) #y ekseni ile ilgili ayarlama yapıldı.
    plt.bar(y_pos, hist, align='center', color='r', alpha=0.5)
    plt.xticks(y_pos, y_pos)
    plt.ylabel('Frequency')
    plt.title('Histogram')
    plt.show()


def image_hist(image): # RGB renk uzayını göstermek için kullanılır
    cv.imshow("input", image)
    color = ('blue', 'green', 'red') #rgb renklerde gezerek histogram oluşturuldu
    for i, color in enumerate(color):
        hist = cv.calcHist([image], [i], None, [256], [0, 256]) #Bir veya daha fazla dizinin histogramını hesaplamak için kullanılan fonk.
# ([image], [i], None, [256], [0, 256]) --> 1. parametre = resim, 2.parametre = renklerin indeksleri 4. paramtre --> ayrım noktalarında kutucukları ifade eder. 5.parametre --> histogram boyutu
        plt.plot(hist, color=color)
        plt.xlim([0, 256])
    plt.show()
#Resmi getiren fonk
src = cv.imread("orman.jpg")
cv.namedWindow("input",cv.WINDOW_AUTOSIZE)
cv.imshow("input",src)
cv.waitKey(0)
#Resmi griye döndürme
gray = cv.cvtColor(src,cv.COLOR_BGR2GRAY)
custom_hist(gray)

image_hist(gray)

cv.destroyAllWindows()