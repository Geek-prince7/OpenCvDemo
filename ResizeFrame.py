import cv2 as cv

"""
#to read image
img=cv.imread('Photo/wolf_small.jpg')
#to show the image
cv.imshow('dog',img)
#how much to hold the photo window 0 means infinite
cv.waitKey(0)
"""



#to resize the frame
def resize_frame(frame,scale=0.75):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    return cv.resize(frame,(width,height), interpolation=cv.INTER_AREA)

## Reading Videos
capture=cv.VideoCapture(0)
while True:
    isTrue,Frame=capture.read()
    new_frame=resize_frame(Frame)
    cv.imshow('Video',new_frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()
