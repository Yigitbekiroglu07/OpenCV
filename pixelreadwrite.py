import cv2 as cv #OpenCV kütüphanesi cv ile çağrılır.

path="opencvr.png" # resmin yolu(adresi)
img = cv.imread(path) #ilgili resmin dizinini ver, resmi okur
cv.namedWindow("img", cv.WINDOW_AUTOSIZE) # kendin isim ver, resmin boyutunu koru

h,w,ch=img.shape #uzunluk,genişlik,rgb(kanal bilgisi) bilgileri tutulur.
print("h,w,ch",h,w,ch)

for row in range(h): #İki kere gezilerek resmin rengi değiştirilir. 
    for col in range(w):
        b,g,r = img[col,row]
        b = 255-b
        g = 255 -g
        r = 255- r
        
    img[row,col]=[b,g,r] #siyahlar beyaz, beyazlar siyaha döner.

    
    cv.imshow("output",img)
    cv.waitKey(1)