from django.contrib import admin
from django.urls import path,include
from core.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('', frontpage,name='frontpage'),
    path('aboutPage/', aboutPage,name='aboutPage'),
    path('yourDates/',yourDates,name='yourDates'),
    path('img',img,name='img'),    
    path('login/', login_user,name='login'),
    path('logout/', logout_user,name='logout'),
    path('products/', products,name='products'),
    path('register/',register_user,name='register'),
    path('update_user/',update_user,name='update_user'),
    path('update_password/',update_password,name='update_password'),
    path('update_info/',update_info,name='update_info'),
    path('product/<int:pk>', product,name='product'),
    path('categories/<str:name>', categories,name='categories'),



]

