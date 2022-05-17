import cv2 as cv
import numpy as np

img=cv.imread('Photo/zebra1_small.jpg')
cv.imshow('img',img)

#edges and gradients

#grayscale
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)


#1.laplacian edges
lap=cv.Laplacian(gray,cv.CV_64F)
lap=np.uint8(np.absolute(lap))
cv.imshow('laplacian edges',lap)


#2.sobel
#sobel can computes  for x and y direction
sobelx=cv.Sobel(gray,cv.CV_64F,1,0)
sobely=cv.Sobel(gray,cv.CV_64F,0,1)

cv.imshow('Sobel-x',sobelx)
cv.imshow('Sobel-y',sobely)
#we can combine both sobel images
combined=cv.bitwise_or(sobelx,sobely)
cv.imshow('combined sobel',combined)

# 3.canny edge detector
canny=cv.Canny(gray,125,175)
cv.imshow('canny',canny)



cv.waitKey(0)