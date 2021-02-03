from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def Index(request):
     return render(request, 'MainApp/index.html')

def Login(request):
     return render(request, 'MainApp/Login.html')

def Register(request):
     return render(request, 'MainApp/Register.html')


