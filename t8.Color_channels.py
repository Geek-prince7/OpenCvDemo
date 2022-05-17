import cv2 as cv
import numpy as np

img=cv.imread('Photo/dog2_small.jpg')
cv.imshow('Image',img)


#splitiing image into blue ,green and red
b,g,r=cv.split(img)
#these image will be in grayscale
cv.imshow('blue',b)
cv.imshow('green',g)
cv.imshow('red',r)

#merging image
merged_img=cv.merge([b,g,r])
cv.imshow('Merged image',merged_img)

#printing shape
print(img.shape)
print(merged_img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

#we can create img in r,g,b in any one
blank=np.zeros(img.shape[:2],dtype='uint8')
red_img=cv.merge([blank,blank,r])
green_img=cv.merge([blank,g,blank])
blue_img=cv.merge([b,blank,blank])
cv.imshow('Red_img',red_img)
cv.imshow('Green_img',green_img)
cv.imshow('Blue_img',blue_img)


cv.waitKey(0)