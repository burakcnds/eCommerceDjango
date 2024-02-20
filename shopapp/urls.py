from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('products/<slug:d_slug>/',products,name='products'),
    path('productsDetail/<slug:d_slug>/', productDetail, name='productsDetail'),
    path('sepet',sepet,name='sepet')


    
    
]
