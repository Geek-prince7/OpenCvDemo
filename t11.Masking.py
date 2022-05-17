import cv2 as cv
import numpy as np

img=cv.imread('Photo/nature1_small.jpg')
cv.imshow('image',img)

#masking allow to focus on certain part of image
#use --> if we have pic of people and we want to focus on face we can do that

#its imp that shape is same for masking Ow wont work
blank=np.zeros((img.shape[0:2]),dtype='uint8')
#draw circle or rectangle
circle=cv.circle(blank.copy(),(img.shape[1]//2,img.shape[0]//2),100,255,-1)
cv.imshow('circle',circle)

#we cant simply use bitwise and on img and mask it wont work
masked=cv.bitwise_and(img,img,mask=circle)
cv.imshow('and operator',masked)

#we can try on a weird shape too
rectngle=cv.rectangle(blank.copy(),(200,200),(400,400),255,-1)
cv.imshow('rectangle',rectngle)

newShape=cv.bitwise_or(rectngle,circle)
cv.imshow('new shape',newShape)

#mask using newshape
maseked2=cv.bitwise_and(img,img,mask=newShape)
cv.imshow('new masked image',maseked2)

cv.waitKey(0)