import re
from urllib import response
from django.shortcuts import render

# Create your views here.
def setcokie(request):
    response=render(request,'students/setcokie.html')
    response.set_cookie('name','jayant',max_age=120)  # max_age is setting the limit of cokkie and then it will expire
    # or expries=datetime.utcnow()+timedelta(days=2) for setting cookie for dayes
    return response
def getcokie(request):
    #name=request.COOKIES['name']
    name=request.COOKIES.get('name','Guest')  #  Benift of using this way is we can set default value as none but in first wat it will give us error if add unknown key
    # this guest is seconf default name so instead of none guest will appear only if we delete cokkie
    return render(request,'students/getcokie.html',{'name':name})
def delcookie(request):
    response=render(request,'students/getcokie.html')
    response.delete_cookie('name')
    return response