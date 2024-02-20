from django.urls import path
from .views import *

urlpatterns = [
    path('account/',account,name='account'),
    path('profile/',profile,name='profile'),
    path('logout/', userLogout, name='userLogout'),
   
    
]
