import cv2 as cv

capture = cv.VideoCapture(0) #Video okuma methodu, 0 dahili kamera için kullanılır.
height = capture.get(cv.CAP_PROP_FRAME_HEIGHT)#Videonun yüksekliği
width = capture.get(cv.CAP_PROP_FRAME_WIDTH)#Videonun genişliği
count = capture.get(cv.CAP_PROP_FRAME_COUNT)
fps = capture.get(cv.CAP_PROP_FPS)#Videonun fps değeri
print(height,width,count,fps)

def process(image, opt=1): # Videoyu canlı olarak işleme imkanı verir, img = video, option koşulları ifade eder otomatik 1 dedik.
    dst= None
    if opt == 0:
        dst = cv.bitwise_not(image) #Renkleri tersine çevirme işlemi yapar.
    if opt == 1:
        dst = cv.GaussianBlur(image,(0,0),15) #Görüntüyü bulanıklaştırma
    if opt == 2:
        dst = cv.Canny(image,100,200) #Görüntüde kenarlar algılanır.
    return dst
    
index = 2 #yukarıdaki option'u ifade eder --> index=opt
while True:
    ret,frame = capture.read() #True olduğu sürece capture'da ne varsa oku
    if ret is True:
            cv.imshow("kamera",frame) #Okuma gerçekleşirse kamerayı göster
            c=cv.waitKey(50)
            if c>=49:
                index = c-49
            result = process(frame,index)
            cv.imshow("result",result)
            #print c
            if c ==27: #ESC
                 break
    else:
            break
        
cv.waitKey(0)
                 