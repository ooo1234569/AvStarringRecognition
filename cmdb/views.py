from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.conf import settings
import os,cv2,face_recognition
import cmdb.model
# Create your views here.
import numpy as np
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
    print(result)
    for k in result:

        k,url=k.split(' ')
        temp=k.replace('__1','').replace('face\\','')
        temp2=getfanhao(os.path.basename(temp))
        dic['l' + str(num)] = 'https://www.javbus.pw/'+temp2
        dic['image' + str(num)]=url
        num=num+1
    return render(request, 'result.html',dic)

def getfanhao(s):
    print(s)
    shuzi=['0','1','2','3','4','5','6','7','8','9']
    temp=s.split('-')
    print(temp)
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






