from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()


class Profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    profileimg=models.ImageField(upload_to='profile_file',default='blank.webp')
    
