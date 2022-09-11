from django.shortcuts import render
from .models import Chat,Group
# Create your views here.
def index(request):
   return render(request,'home.html')
def show(request,group_name): 
   print(group_name)
   group=Group.objects.filter(name=group_name).first()
   chats=[]
   if group:
     chats=Chat.objects.filter(group=group)

   else:
     group=Group(name=group_name)
     group.save()    
   print(chats)
   return render(request,'home.html',{'group_name':group_name,'Chats':chats})