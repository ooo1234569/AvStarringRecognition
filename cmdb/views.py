from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.conf import settings
import os,cv2,face_recognition
import cmdb.model
# Create your views here.
import numpy as np

face_patterns = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
def index(req):
    return render(req, 'file.html')

def upload(request):
    obj = request.FILES.get('fileUpload')
    f=open(obj.name,'wb')
    for chunk in obj.chunks():  # 分块写入文件
        f.write(chunk)
    f.close()
    result=cmdb.model.classify(obj.name)
    dic={}
    num=1
    for k in result:
        print(k)
        temp=k.split('AvStarringRecognition\\')[1].replace('__1','').replace('face\\','')
        dic['image'+str(num)]=temp
        temp2=getfanhao(os.path.basename(temp))
        print(temp2)
        dic['l' + str(num)] = 'https://www.javbus.pw/'+temp2
        num=num+1
    return render(request, 'result.html',dic)

def getfanhao(s):
    shuzi=['0','1','2','3','4','5','6','7','8','9']
    temp=s.split('-')
    qianzhui = temp[0]
    s2 = temp[1]
    if len(temp)>2:
        s2=s2+temp[2]
    qianzhui=qianzhui+'-'
    for i in s2:
        if i in shuzi:
            qianzhui=qianzhui+i
        else:
            break
    return qianzhui






