import numpy as np
import cv2 as cv

src = cv.imread("blok.jpg")

def process(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    corners = cv.goodFeaturesToTrack(gray, maxCorners=35, qualityLevel=0.05, minDistance=10) #Görüntüdeki en belirgin köşeleri bulur.
    for pt in corners:
        print(pt)
        b = np.random.randint(0, 256)
        g = np.random.randint(0, 256)
        r = np.random.randint(0, 256)
        x = np.int32(pt[0][0])
        y = np.int32(pt[0][1])
        cv.circle(image, (x, y), 5, (int(b), int(g), int(r)), 2)
    return image

result = process(src)
cv.imshow("result",result)
cv.waitKey(0)