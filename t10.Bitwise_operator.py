import cv2 as cv
import numpy as np

# img=cv.imread('Photo/leopard1.jpg')
# cv.imshow('leopard',img)
blank=np.zeros((400,400),dtype='uint8')
#draw a rectangle and circle
rectangle=cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
circle=cv.circle(blank.copy(),(200,200),200,255,-1)
cv.imshow('rectangle',rectangle)
cv.imshow('circle',circle)

#bitwise operator operates in binary manner

#1.bitwise and
#return intersection
bit_and=cv.bitwise_and(rectangle,circle)
cv.imshow('Bitwise and',bit_and)


#2.bitwise or
#union of both image
bit_or=cv.bitwise_or(rectangle,circle)
cv.imshow('bitwise OR',bit_or)

#3.bitwise XOR
#return union-intersection
bit_xor=cv.bitwise_xor(rectangle,circle)
cv.imshow('Bitwise XOR',bit_xor)

#4. bitwise NOT
bit_not1=cv.bitwise_not(rectangle)
cv.imshow('Bitwise not rectangle',bit_not1)

bit_not2=cv.bitwise_not(circle)
cv.imshow('Bitwise not circle',bit_not2)




cv.waitKey(0)