import cv2,pickle,face_recognition,os
import numpy as np
m = None
bp=r'C:\Users\bingnan\PycharmProjects2\AvStarringRecognition\\'
class Model(object):
    def __init__(self):
        self.face_patterns = cv2.CascadeClassifier(
            r'C:\Users\bingnan\PycharmProjects\AvStarringRecognition\test\haarcascade_frontalface_default.xml')
        print('加载模型中')
        kfile = open(r'C:\Users\bingnan\PycharmProjects\AvStarringRecognition\test\feature.dat', 'rb')
        self.k = pickle.load(kfile)
        lfile = open(r'C:\Users\bingnan\PycharmProjects\AvStarringRecognition\test\lable.dat', 'rb')
        self.lables = pickle.load(lfile)
        print('加载模型完成')

    def classify(self,name):
        rr={}
        sample_image = self.cv_read(bp+name)
        faces = self.face_patterns.detectMultiScale(sample_image, scaleFactor=1.1, minNeighbors=5, minSize=(100, 100))
        for (x, y, w, h) in faces:
            temp = sample_image[y:y + h, x:x + w]
            cv2.imencode('.jpg', temp)[1].tofile(
                'temp.jpg')
        tocompare = face_recognition.face_encodings(face_recognition.load_image_file('temp.jpg'))[0]
        result = face_recognition.face_distance(self.k, tocompare)
        dic = {}
        for r in range(len(result)):
            dic[self.lables[r]] = result[r]
        dic = sorted(dic.items(), key=lambda x: x[1], reverse=False)
        num = 0
        tempname = None
        for d in dic:
            if num < 6:
                if os.path.basename(d[0]) != tempname:
                    rr[d[0]]=d[1]
                    print(d[0] + ":" + str(d[1]))
                    num = num + 1
                    tempname = os.path.basename(d[0])
                else:
                    continue
            else:
                break
        return rr

    def cv_read(self,path):
        cv_img = cv2.imdecode(np.fromfile(path, dtype=np.uint8), -1)
        return cv_img


if m is None:
    m = Model()

def classify(name):
    return m.classify(name)

