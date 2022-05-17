import cv2 as cv
import numpy as np

img=cv.imread('Photo/dog2_small.jpg')
cv.imshow('Orignal Image',img)

"""
#translation
def translation(img,x,y):
    transMat=np.float32([[1,0,x],[0,1,y]])
    dimensions=(img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)

# x -->left
# -x -->right
# y -->down
# -y --> up

translated_img=translation(img,100,100)
cv.imshow("translated 1",translated_img)
"""

"""
#ROTATION
def rotate(img,angle,rotPoint=None,scale_val=1.0):
    width,height=img.shape[1],img.shape[1]
    if rotPoint is None:
        rotPoint=(width//2,height//2)
    rotMat=cv.getRotationMatrix2D(rotPoint,angle,scale_val)
    dimensions=(width,height)
    return cv.warpAffine(img,rotMat,dimensions)

# -angle --> roate right
# angle -->rotete left
rotated_image=rotate(img,45)
cv.imshow('rotated img',rotated_image)

"""

#flipping
#flip_code val -
# 0 --> vertically
# 1 --> horizontally
# -1--> both vert and horizontally
flipped=cv.flip(img,1)
cv.imshow('flipped img',flipped)


cv.waitKey(0)