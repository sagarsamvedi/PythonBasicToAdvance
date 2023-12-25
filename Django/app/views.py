from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import *
# Create your views here.

def index(request):
    return render(request,'form.html')

def welcome(request):
    return render(request,'welcome.html')

def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        if User.objects.filter(email =email).exists():
            return HttpResponse("email already exist")
        else:
            User.objects.create(name = name, email =email, phone = phone, password = password)
            return redirect('/welcome/')