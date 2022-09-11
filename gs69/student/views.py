import re
from urllib import response
from django.shortcuts import render

# Create your views here.
def setcokie(request):
    response=render(request,'students/setcokie.html')
    response.set_signed_cookie('name','vikas',salt='nm')
    return response
def getcokie(request):
    name=request.get_signed_cookie('name',salt='nm')
    return render(request,'students/getcokie.html',{'name':name})
def delcookie(request):
    response=render(request,'students/getcokie.html')
    response.delete_cookie('name')
    return response