import cv2 as cv
import numpy as np

img=cv.imread('Photo/hawk1.jpg')
cv.imshow('image',img)

#thresholding - converting image to binary eith 0(black) or 255(white).we ll set a treshold value and compare with each pixel
#if pixel<threshold then 0(black) else 255(white)


gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('grayscale',gray)

#1.simple thresholding
threshold,thresh=cv.threshold(gray,120,255,cv.THRESH_BINARY)
cv.imshow('simple threshold img',thresh)

#inverse thresholded image
threshold,thresh_inverse=cv.threshold(gray,120,255,cv.THRESH_BINARY_INV)
cv.imshow('inverse threshold image',thresh_inverse)

#2.Adaptive thresholding
#adaptive thresholding --> we dont need to pass threshold value manually instead algo will auto find optimal threshold value
#adaptive_thresh_mean -->find kernel grid and findmean of its neighbor here kernel size is 11x11
#instead of cv.ADAPTIVE_THRESH_MEAN_C we can use -adaptive thresh gaussian - assign weight and compute mean across those pixels

adaptive_thresh=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,3)
cv.imshow('Adaptive thresholding',adaptive_thresh)


cv.waitKey(0)
