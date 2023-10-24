from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    
    path('',Login,name='Login'),
    path('register/',Register,name='Register'),
    path('Logout/',Logout,name='Logout'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)