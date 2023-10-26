from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from chats.models import UserProfileModel

# Create your views here.
def Login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user_login=authenticate(username=username,password=password)
        if user_login:
           login(request,user_login)
           return redirect('home')
        messages.info(request,'login Unsuccesfully')
        return redirect('Login')
    return render(request,'login.html')

def Register(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        image=request.FILES.get('File')

        print(username,password,image)

        user=User.objects.filter(username=username)
        if user:
            messages.info(request,'Username already token')
            return redirect('Register')
        else:
            user=User.objects.create_user(username=username,email='',password=password)
            user.save()

            user_login=authenticate(username=username,password=password)
            login(request,user_login)

            user_obj=User.objects.get(username=username)
            UserProfileModel.objects.create(user=user_obj)

            new_profile=Profile.objects.create(user=user_obj,profileimg=image)
            new_profile.save()
            messages.info(request,'Account created successfully')
            return redirect('Login')
    
    return render(request,'signup.html')

def Logout(request):
    logout(request)
    return redirect('Login')