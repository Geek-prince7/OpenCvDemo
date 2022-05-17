# t4


import cv2 as cv
img=cv.imread('Photo/dog2_small.jpg')
cv.imshow('dog',img)

"""
#converting to grayscale
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('grayscale',gray)
"""

"""
#blur image
blur=cv.blur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow('blur',blur)
"""
"""
#edge cascade
canny=cv.Canny(img,125,175)
#canny2=cv.Canny(blur,125,175)
cv.imshow('cannyyy',canny)
#cv.imshow('cannyyy2',canny2)



#dilating the image
dilated=cv.dilate(canny,(7,7),iterations=3)
cv.imshow('dilated',dilated)


#erode
eroded=cv.erode(dilated,(7,7),iterations=3)
cv.imshow('erode means change dilated image to back self', eroded)
"""


#Resize
resized=cv.resize(img,(800,500),interpolation=cv.INTER_AREA)
#cv.inter_area if we want new img smaller than org but if we want to enlarge it we use cv.INTER_LINEAR or cv.INTER_CUBIC
cv.imshow('resized img',resized)

#cropping
#images are like array so we can use array slicing
cropped=img[70:600,200:800]
cv.imshow('cropped img',cropped)



cv.waitKey(0)
