import numpy as np
import cv2
dataset = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
face_1 = np.load('face_1.npy').reshape((20,50*50*3))
face_2 = np.load('face_1.npy').reshape((20,50*50*3))
font = cv2.FONT_HERSHEY_SIMPLEX
names = {
    0 : 'user_1',
    1 : 'user_2'
}
labels = np.zeros((40,1))
labels[0:20, :] = 0.0
labels[20:, :] = 1.0

data = np.concatenate([face_1, face_2])
def distance(x1,x2):
    return np.sqrt(((x1 - x2)**2).sum())
def knn(x, train, k = 5):
    m = train.shape[0]
    dist = []
    for i in range(m):
        dist.append(distance(x, train[i]))
    dist = np.asarray(dist)
    index = np.argsort(dist)
    sorted_labels = labels[index][:k]
    counts = np.unique(sorted_labels, return_counts=True)
    print(counts)
    return counts[0][np.argmax(counts[1])]

while True:
    ret, img = cap.read()
    if ret:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = dataset.detectMultiScale(gray, 1.3)
        for x,y,w,h in faces:
            face_comp = img[y:y+h,x:x+w,:]
            fc = cv2.resize(face_comp, (50,50))
            lab = knn(fc.flatten(), data)
            text = names[int(lab)]
            cv2.putText(img, text, (x,y), font, 1, (255,255,0),2)
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)
        cv2.imshow('result',img)
        if cv2.waitKey(1) == 27:
            break
    else:
        print("Some error")
cap.release()
cv2.destroyAllWindows()