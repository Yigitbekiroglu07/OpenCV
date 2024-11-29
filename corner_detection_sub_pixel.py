# subpixel --> Köşe konumlarını iyileştirir
# Diğer yöntemlere göre daha hassas (iyi) sonuçlar verir.
import cv2 as cv
import numpy as np
src = cv.imread("blok.jpg")
def process(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    corners = cv.goodFeaturesToTrack(gray, 100, 0.05, 10)
    print(len(corners))
    for pt in corners:
        print(pt)
        b = np.random.random_integers(0, 256)
        g = np.random.random_integers(0, 256)
        r = np.random.random_integers(0, 256)
        x = np.int32(pt[0][0])
        y = np.int32(pt[0][1])
        cv.circle(image, (x, y), 5, (int(b), int(g), int(r)), 2)
    # Kullanılacak yönteme ait parametreler
    winSize = (3, 3) # Arama penceresinin yan uzunluğunun yarısı
    zeroZone = (-1, -1) # Arama bölgesinin ortasındaki ölü bölgenin yarısı demek
    
    criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_COUNT, 40, 0.001) #Yinelemeli köşe iyileştirme bilgisinin ne zaman sonlanacağı ile ilgili bilgi verir.
    corners = cv.cornerSubPix(gray, corners, winSize, zeroZone, criteria)

    for i in range(corners.shape[0]): #Köşelerle ilgili raporlama yapmak için
        print("-- Refined Corner [", i, "] (", corners[i, 0, 0], ",", corners[i, 0, 1], ")")
    return image  

result = process(src)
cv.imshow("result",result)
cv.waitKey(0)

