import cv2 as cv

"""
#to read image
img=cv.imread('Photo/wolf_small.jpg')
#to show the image
cv.imshow('dog',img)
#how much to hold the photo window 0 means infinite
cv.waitKey(0)
"""




## Reading Videos
capture=cv.VideoCapture(0)
while True:
    isTrue,Frame=capture.read()
    cv.imshow('Video',Frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()
