import cv2

img=cv2.imread('solar-system.jpg')
cv2.putText(img,"Sun",(20,180),cv2.FONT_HERSHEY_COMPLEX,1.0,(255,0,0))
cv2.putText(img,"Mercury",(110,260),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"Venus",(200,260),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"Earth",(290,260),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"Moon",(325,160),cv2.FONT_HERSHEY_COMPLEX,0.3,(255,255,255))
cv2.putText(img,"Mars",(380,260),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"Jupiter",(540,370),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"Saturn",(770,290),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"Uranus",(970,290),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"Mercury",(1110,290),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.imshow('output',img)
cv2.waitKey(0)

 

 