import cv2

#Loading The Cascade File
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

image = cv2.imread('lms.png') #C:\Users\v-navmittal\Desktop\lms.png

img = cv2.resize(image, (600, 400))

imggray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Detecting The Faces
faces = face_cascade.detectMultiScale(imggray, 1.2, 5)

#Pointing The Faces
for (x,y,w,h) in faces:
	cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0),2)

#Displaying The Output Image
cv2.imshow('img', img)
cv2.waitKey()
