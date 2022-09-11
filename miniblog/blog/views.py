from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
# Create your views here.
def user_login(request):
    return render(request,'blog/login.html')
def Home(request):
    return render(request,'blog/home.html')
def About(request):
    return render(request,'blog/about.html')
def Contact(request):
    return render(request,'blog/contact.html')
def DashBoard(request):
    return render(request,'blog/dashboard.html')
def user_logout(request):
    return HttpResponseRedirect(request,'')
def SignUp(request):
    form=SignUpForm()
    return render(request,'blog/signup.html',{'form':form})