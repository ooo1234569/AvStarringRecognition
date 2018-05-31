from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.

def index(req):
    return render(req, 'file.html')

def upload(request):
    obj = request.FILES.get('fileUpload')
    return HttpResponse(obj.name)