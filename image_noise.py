# Piksellerin dışında kalan bölgeler gürültü olarak ifade edilir.
import cv2 as cv
import numpy as np

path = "opencvr.png"
src = cv.imread(path)

def add_salt_pepper_noise(image):
    h, w = image.shape[:2]  # Resmin boyutu
    nums = 10000
    rows = np.random.randint(0, h, nums, dtype=int)  # np.int yerine int kullanıldı
    cols = np.random.randint(0, w, nums, dtype=int)  # np.int yerine int kullanıldı
    for i in range(nums):
        if i % 2 == 1:
            image[rows[i], cols[i]] = (255, 255, 255)  # Beyaz noktalar (tek sayılar)
        else:
            image[rows[i], cols[i]] = (0, 0, 0)  # Siyah noktalar (çift sayılar)
    return image

h, w = src.shape[:2]  # Resmin boyutları alınır

copy = np.copy(src)  # Resmin kopyası alınır
copy = add_salt_pepper_noise(copy)  # Gürültü fonk eklenir

# Resmin ilk haliyle üzerinde gürültü eklenmiş halini birleştirmek için
result = np.zeros([h, w * 2, 3], dtype=src.dtype)
result[0:h, 0:w, :] = src
result[0:h, w:2 * w, :] = copy

# Sonuç görüntüsü
cv.imshow("Result", result)
cv.waitKey(0)
cv.destroyAllWindows()

