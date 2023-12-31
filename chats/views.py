from django.shortcuts import render
from django.contrib.auth import get_user_model
from .models import *
from django.contrib.auth.decorators import login_required
from account.models import *


# Create your views here.
User=get_user_model()

@login_required(login_url='Login')
def home(request):
    users=User.objects.exclude(username=request.user.username)
    users1=User.objects.get(username=request.user.username)
    print(users1.id)
    profile=Profile.objects.exclude(user=users1)
    print(profile)
    return render(request,'index.html',context={'users': users, 'prof': profile})
     

                                                          


@login_required(login_url='Login')
def chatPage(request, username):
    user_obj=User.objects.get(username=username)
    user_status=UserProfileModel.objects.get(user=user_obj)
    users=User.objects.get(username=request.user.username)
    user_prof=Profile.objects.get(user=users)
    profile=Profile.objects.exclude(user=users)
    profile_obj=Profile.objects.get(user=user_obj)

    if request.user.id > user_obj.id:
        thread_name = f'chat_{request.user.id}-{user_obj.id}'
    else:
        thread_name = f'chat_{user_obj.id}-{request.user.id}'

    

    message_obj=ChatModel.objects.filter(thread_name=thread_name) 
    
    return render(request,'main_chat.html',context={'prof':profile,'user1':profile_obj,'messages': message_obj,'userprof':user_prof,'user':user_obj,'status':user_status})
