import cv2 as cv
import numpy as np


#face detection is diff from face recognition
#face detection -->detects a face in an image
#face recognition involves identifying whose face it is.


img=cv.imread('Photo/anaisha1.jpg')
#cv.imshow('Person',img)


gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#cv.imshow('gray',gray)

haar_cascade=cv.CascadeClassifier('haar_face.xml')
faces_rect=haar_cascade.detectMultiScale(gray,1.1,5)
print(len(faces_rect))


for (x,y,w,h) in faces_rect:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
cv.imshow('detected face',img)

cv.waitKey(0)


###############################################################
#detecting video

# capture=cv.VideoCapture(0)
# while True:
#     isTrue,Frame=capture.read()
#     haar_cascade = cv.CascadeClassifier('haar_face.xml')
#     faces_rect=haar_cascade.detectMultiScale(Frame,1.1,5)
#     for (x, y, w, h) in faces_rect:
#         cv.rectangle(Frame,(x,y),(x+w,y+h),(0,0,255),2)
#
#     cv.imshow('Video',Frame)
#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break
