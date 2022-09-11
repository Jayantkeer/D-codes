import re
from urllib import response
from django.shortcuts import render

# Create your views here.
def setsession(request):
    request.session['name']='ramesh'
    return render(request,'students/setsession.html')
def getsession(request):
    name=request.session['name']  # that get method is same as cookie
    return render(request,'students/getsession.html',{'name':name})
def delsession(request):
    if 'name' in request.session:
        del request.session['name']
    return render(request,'students/deletesession.html')