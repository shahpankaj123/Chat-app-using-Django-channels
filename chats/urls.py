from django.urls import path
from .views import *


urlpatterns = [
    
    path('',home),
    path('chat/<str:username>',chatPage,name='chat'),
]