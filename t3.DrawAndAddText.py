import cv2 as cv
import numpy as np


#to draw a blank image
blank=np.zeros((500,500,3), dtype='uint8')
cv.imshow('blank',blank)

"""
# 1. Paint the image with certain color
blank[:]=0,255,0
cv.imshow('green',blank)
"""
"""
# 2. Paint the image to create a rectangle
blank[200:300,300:400]=0,255,0
cv.imshow('green',blank)
"""
"""
#3. draw a rectangle
cv.rectangle(blank,(0,0),(250,500),(255,0,255),thickness=4)
#if thickeness=cv.FILLED or -1 then it will fill inner part of it too
cv.imshow('rectamgle',blank)
"""

"""
#4. draw a circle
cv.circle(blank,(200,200),40,(255,0,255),thickness=-1,)
#if thickeness=cv.FILLED or -1 then it will fill inner part of it too
cv.imshow('Circle',blank)
"""
"""
#5. Draw a line
cv.line(blank,(10,10),(200,300),(0,0,255),thickness=2)
cv.imshow('line',blank)
"""
#6. mix of circle,line and rectangle
cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(255,0,255),thickness=-1)
cv.circle(blank,(250,250),40,(255,255,255),thickness=-1)
cv.line(blank,(10,10),(250,250),(0,0,255),thickness=7)
#cv.imshow('mix draw',blank)

#7. Add text on image
cv.putText(blank,'Hello',(300,300),cv.FONT_ITALIC,1.0,(0,255,0),2)
cv.imshow('mix draw',blank)

cv.waitKey(0)