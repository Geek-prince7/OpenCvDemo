import cv2 as cv
import matplotlib.pyplot as plt

img=cv.imread('Photo/wolf_small.jpg')
cv.imshow('wolf',img)

#grayscale
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)


#BGR to HSV
hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('hsv',hsv)


#BGR to LAB
lab=cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('LAB',lab)

"""

#outside of opencv if we read any color image it will be inverted because in open cv format -RGB outside-BGR
plt.imshow(img)
plt.show()
"""
#BGR to RGB
rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('RGB',rgb)



#we cant directly convert grayscale to lab
#we need to convert grayscale to bgr then bgr to lab
#same for all first convert to bgr then bgr to other





cv.waitKey(0)