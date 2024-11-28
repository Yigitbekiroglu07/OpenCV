# Histogram Eşitleme = Histogram dağılımının daha eşit olmasını sağlamak. Zıtlık yaratmak için yaparız. Resimde iyileşitrme yapılmış olur.
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
# Histogram --> Sayısal değişkenlerin dağılımını göstermek için kullanılan grafik yöntem
def custom_hist(gray): #Gri resimleri göstermek için kullanılır
    h, w = gray.shape #Görselin boyut bilgileri alınır
    hist = np.zeros([256], dtype=np.int32) # 0'dan 256'ya kadar boş değer oluşturuldu
    for row in range(h):
        for col in range(w):
            pv = gray[row, col]
            hist[pv] += 1

    y_pos = np.arange(0, 256, 1, dtype=np.int32)
    plt.bar(y_pos, hist, align='center', color='r', alpha=0.5)
    plt.xticks(y_pos, y_pos)
    plt.ylabel('Frequency')
    plt.title('Histogram')
    plt.show()
    
src = cv.imread("orman.jpg")
gray = cv.cvtColor(src,cv.COLOR_BGR2GRAY)
cv.imshow("input",gray)
cv.waitKey(0)
    
custom_hist(gray)
    
dst = cv.equalizeHist(gray) # Histogram eşitleme fonk. Görüntülerin histogramlarını eşitler.
cv.imshow("eh",dst)
cv.waitKey(0)
    
custom_hist(dst)