import cv2 as cv
import numpy as np

img=cv.imread('Photo/dog2_small.jpg')
cv.imshow('Orignal Image',img)

#convert to greyscale
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)



"""
#edge cascade on grayscale img
canny=cv.Canny(gray,125,175)
cv.imshow('canny edges',canny)


#gettin contours
#contours - list of counters
contours,hierarchies=cv.findContours(canny,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
print(len(contours), " countours found")
"""

#threshold
#125-thresh val <125 become 0 black
#thresh val >125 become 255 white
#method is THRESH_BINARY so only two color
ret,thresh=cv.threshold(gray,125,255,cv.THRESH_BINARY)
cv.imshow('THRESHOLD',thresh)


#gettin contours
#contours - list of counters
contours,hierarchies=cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
print(len(contours), " countours found")


#NOW CRATE A BLANK IMAGE OF SAME DIMENSION AS IMAGE AND DRAW THESE CONTOURS OVER IT
blank=np.zeros(img.shape,dtype='uint8')
cv.imshow('blank',blank)

#draw contours on blank
# -1 --> ALL LIST OTHERWISE WE CAN USE SEPERATE PORTION TOO
# COLOR - TOWHICH COLOR WE WANT TO DRAW CONTOUR
cv.drawContours(blank,contours,-1,(0,0,255),1)
cv.imshow('contours drawn on blank',blank)


cv.waitKey(0)