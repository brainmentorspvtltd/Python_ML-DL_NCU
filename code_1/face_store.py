import cv2
import numpy as np

dataset = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

data = list()

while True:
    ret,img = cap.read()
    if ret:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = dataset.detectMultiScale(gray)

        for x,y,w,h in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)

            face_comp = img[y:y + h, x:x + w, :]
            fc = cv2.resize(face_comp, (50,50))

            if x % 10 == 0 or len(data) < 20:
                data.append(fc)

        cv2.imshow('result',img)
        if cv2.waitKey(33) == 27 or len(data) >= 20:
            break
    else:
        print("There is some error")

data = np.asarray(data)
np.save('face_1', data)

cap.release()
cv2.destroyAllWindows()