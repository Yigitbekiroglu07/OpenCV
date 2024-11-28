import cv2 as cv

cap = cv.VideoCapture("akdeniz.mp4")

fgbg = cv.createBackgroundSubtractorMOG2(history=250,varThreshold=250)
# varThreshold, odaklanılacak görüntüde ne kadar hassas olunacağını söyler.
# history, gecikmelere ne kadar odaklanacağı. Video akarkenki her bir pencere.
while True:
    ret, frame = cap.read() #Video bilgisi
    fgmask = fgbg.apply(frame) #Siyah arkaplan
    background = fgbg.getBackgroundImage() #Arka plan görüntüsü hesaplanması
    cv.imshow("input",frame)    
    cv.imshow("mask",fgmask)  
    cv.imshow("background",background)  
    k = cv.waitKey(10)&0xff
    if k==27:
        break

cap.release() #Videoyu kapatma
cv.destroyAllWindows() #Pencereyi kapatma