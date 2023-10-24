from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    
    path('',Login,name='Login'),
    path('register/',Register,name='Register'),
    path('Logout/',Logout,name='Logout'),
]
