import cv2
import numpy as np

kamera=cv2.VideoCapture(0)
dusuk=np.array([90,50,50])
yuksek=np.array([130,255,255])

while True:
    ret,kare=kamera.read()
    
    hsv=cv2.cvtColor(kare,cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(hsv,dusuk,yuksek)
    
    son_resim=cv2.bitwise_and(kare,kare,mask=mask)
    
    kernel=np.ones((5,5),np.uint8)
    erosion=cv2.erode(mask,kernel,iterations=1)#SPESİFİK HALE GETİRMEYE BAŞLIYOR
    diolation=cv2.dilate(mask,kernel,iterations=1)#BÜTÜNSEL YAPMAYA ÇALISIYOR
    opening=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)#YİĞİDİN MALI MEYDANDADIR
    closing=cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)#KUSUR KAPATICI
    cv2.imshow("Opening",opening)
    cv2.imshow("Closing",closing)
    cv2.imshow("Erosion",erosion)
    cv2.imshow("diolation",diolation)
    cv2.imshow("son_Resim",son_resim)
    cv2.imshow("mask",mask)
    if cv2.waitKey(25) & 0xFF==ord('q'):
        break











kamera.release()
cv2.destroyAllWindows()
