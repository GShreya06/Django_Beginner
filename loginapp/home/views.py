from ast import Name
from datetime import datetime
from multiprocessing import context
from urllib.request import Request
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , logout , login

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'index.html')


def loginUser(request):
    if request.method == "POST":
        # check if user has correctly entered credentials
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        
        user = authenticate(username = username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/")
        else:
            return render(request, 'login.html')
            

            # No backend authenticated the credentials
    return render(request, 'login.html')


def logoutUser(request):
    logout(request)
    return redirect('/login')
