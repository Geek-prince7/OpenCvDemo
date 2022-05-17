#get pixel distribution in the image in histogram
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
img=cv.imread('Photo/nature3.jpg')
cv.imshow('image',img)

#we are gonna create a histo for rgb images and for grayscale image
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

#grayscale histogram
gray_hist=cv.calcHist([gray],[0],None,[256],[0,256])

plt.figure()
plt.title('Grayscale histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.show()


cv.waitKey(0)