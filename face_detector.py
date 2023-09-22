# install libary for face detection using pip install opencv-python
# upload an image with face and put it in small file
# 
import cv2

face_cascade = cv2.CascadeClassifier('haarcasade_frontalface_default.xml')
img = cv2.imread('faces 2.jpeg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # convert image to gray

faces = face_cascade.detectMultiScale(gray, 1.1, 4)

for (x, y, w, h) in faces:
    cv2.rectangle(img,(x,y),(x+ w, y+h), (225,0,0),2) #draw rectangle around faces
    
cv2.imshow('img',img) # show faces detected
cv2.waitKey()

cv2.imwrite('face_detected.jpeg',img)