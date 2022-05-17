import numpy as np
import cv2 as cv

haar_cascade=cv.CascadeClassifier('haar_face.xml')
people=['jospeh','messi','neymar','paul','ronaldo']

# features=np.load('features.npy')
# labels=np.load('labels.npy')

face_recognizer=cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

pic=cv.imread('testing_photo/ronaldo1.jpg')
img=cv.cvtColor(pic,cv.COLOR_BGR2GRAY)
#cv.imshow('person',img)

#detect face in image
face_rect=haar_cascade.detectMultiScale(img,1.3,6)
for (x,y,w,h) in face_rect:
    face_img=img[y:y+h,x:x+w]

    label,confidence=face_recognizer.predict(face_img)
    print('face class',people[label],'\n','confidence value :',confidence)
    cv.putText(pic,people[label],(30,40),cv.FONT_ITALIC,1.1,(0,0,255),thickness=2)
    cv.rectangle(pic,(x,y),(x+w,y+h),(0,255,0),2)
cv.imshow('person',pic)
cv.waitKey(0)





