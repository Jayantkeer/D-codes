from contextlib import redirect_stderr
from django.shortcuts import render,HttpResponse
from django.contrib.auth import get_user_model

# Create your views here.
def signupAction(request):
    user_model=get_user_model()
    return HttpResponse("user created")
def create_user(request):
    if request.method=='POST':
        email=request.POST['email']
        name=request.POST['name']
        password=request.POST['name']
        user_model=get_user_model()
        user_obj=user_model.objects.create_user(email=email,name=name)
        user_obj.set_password(password)
        user_obj.save()
        return HttpResponse('User is created')
    else:
        return render(request,'signup.hmtl')