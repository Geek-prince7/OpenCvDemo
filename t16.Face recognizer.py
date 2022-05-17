import cv2 as cv
import os
import numpy as np

people=['jospeh','messi','neymar','paul','ronaldo']
dir=r'C:\Users\hp\PycharmProjects\OpenCvDemo\Photo\faces'
haar_cascade=cv.CascadeClassifier('haar_face.xml')

# p=[]
# for i in os.listdir(r'C:\Users\hp\PycharmProjects\OpenCvDemo\Photo\faces'):
#     p.append(i)
# print(p)

features=[]
labels=[]
def train():
    for person in people:
        path=os.path.join(dir,person)
        label=people.index(person)

        for img in os.listdir(path):
            img_path=os.path.join(path,img)

            img_array=cv.cvtColor(cv.imread(img_path),cv.COLOR_BGR2GRAY)
            face_rect=haar_cascade.detectMultiScale(img_array,1.1,4)
            for (x,y,w,h) in face_rect:
                crop_face=img_array[y:y+h,x:x+w]
                features.append(crop_face)
                labels.append(label)

train()
print(len(features))
print(len(labels))

#convert to np array
features=np.array(features,dtype='object')
labels=np.array(labels)

#opencvinbuild face recognizer
face_recognizer=cv.face.LBPHFaceRecognizer_create()

#train the model

face_recognizer.train(features,labels)
face_recognizer.save('face_trained.yml')
np.save('features.npy',features)
np.save('labels.npy',labels)
