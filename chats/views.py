from django.shortcuts import render
from django.contrib.auth import get_user_model
from .models import *

# Create your views here.
User=get_user_model()

def home(request):
    users=User.objects.exclude(username=request.user.username)
    return render(request,'index.html',context={'users':users})

def chatPage(request, username):
    user_obj=User.objects.get(username=username)
    users=User.objects.exclude(username=request.user.username)

    if request.user.id > user_obj.id:
        thread_name = f'chat_{request.user.id}-{user_obj.id}'
    else:
        thread_name = f'chat_{user_obj.id}-{request.user.id}'

    message_obj=ChatModel.objects.filter(thread_name=thread_name) 
    return render(request,'main_chat.html',context={'users':users,'user':user_obj,'messages': message_obj})
