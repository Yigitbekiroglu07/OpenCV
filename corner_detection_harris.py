# Harris --> Köşe Saptama Yöntemi
import cv2 as cv
import numpy as np

path = "chessboard.jpg"
src = cv.imread(path)

def harris(image):
    blockSize = 2 #Köşe tespiti için komşuluk boyutunu ifade eder.
    apertureSize = 3 #Sobel yöntemi için diyafram parametresi
    k = 0.04 #Harris'in serbestlik parametresi

    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    dst = cv.cornerHarris(gray, blockSize, apertureSize, k)
    dst_norm = np.empty(dst.shape, dtype=np.float32)  # `dst_norm` eksikti, eklendi, resimle aynı boyutlarda boş array.
    cv.normalize(dst, dst_norm, alpha=0, beta=255, norm_type=cv.NORM_MINMAX)
    # Köşelerin etrafında dönüp daire şeklini alması için kullanılan döngü
    for i in range(dst_norm.shape[0]):
        for j in range(dst_norm.shape[1]):
            if int(dst_norm[i, j]) > 120:
                cv.circle(image, (j, i), 2, (0, 255, 0), 2)

    return image

result = harris(src)
cv.imshow("result",result)
cv.waitKey(0)
