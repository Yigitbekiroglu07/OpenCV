import cv2 as cv


path = "work.jpg"
src = cv.imread(path)

T=127 #Eşik değer 127 seçildi --> 0-255 arasından

gray = cv.cvtColor(src,cv.COLOR_BGR2GRAY) #Resmi griye çevirme

for i in range(5): # 0'dan 5'e kadar 5 görsel olacak
    ret, binary = cv.threshold(gray,T,255,i) #rastgele i değerlerine göre görsel oluşturacak
    cv.imshow("binary_"+ str(i),binary)
    cv.waitKey(0)
    cv.destroyAllWindows()