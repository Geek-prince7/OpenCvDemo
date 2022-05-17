import cv2 as cv
import numpy as np

img=cv.imread('Photo/nature1_small.jpg')
cv.imshow('Image',img)


#1. Average Blur
#concept -->kernel -->like grid the center of grid for ex for kernel_size =3x3 center box is (2,2) so it ll take the avg of all surronding px
#and the center got the avg value then the table slides to right and repeat and once row 1 is done it'll go to row 2 then row 3
#more the kernel size more the blur is how? --> if kernel size is 3x3 then center is 2,2 then it has 8 neighbors and take avg of those 8
#but if kernel size is 5x5 then center is 3,3 and it has 24 neighbors and itll take avg of 24 .
average=cv.blur(img,(7,7))
cv.imshow('AVerage blur',average)

#2. gaussian blur
#kind of same as average blur its just that in gaussian blur each cell has given some weight so avg of product of weights is the value here
#here the blur is less ict avg blur but looks natural.
gaussian=cv.GaussianBlur(img,(5,5),0)
cv.imshow('Gaussian blur',gaussian)

#3.Median blur
#finds the median of the surrounding pixels
#less blur tha gaussian
#smooth image
median=cv.medianBlur(img,3)
cv.imshow('median',median)

#4. bilateral blurring
#most effective
#bilateral blurring applies blurring but retains the edges of the image
bilateral=cv.bilateralFilter(img,10,35,35)
cv.imshow('bilateral blur',bilateral)

cv.waitKey(0)