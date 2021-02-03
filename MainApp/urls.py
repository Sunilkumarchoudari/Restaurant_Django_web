from django.contrib import admin
from django.urls import path
from  . import views

urlpatterns = [
    path('', views.Index, name='Index.html'),
    path('Login/', views.Login, name='Login.html'),
    path('Register/', views.Register, name='Register.html'),
    
]