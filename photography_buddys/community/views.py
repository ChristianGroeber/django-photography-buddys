from django.contrib import auth
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect


# Create your views here.
from .forms import PhotographerLoginForm


def index(request):
    return render(request, 'community/index.html')


def login(request):
    login_form = PhotographerLoginForm(request.POST or None)
    if request.method == 'GET':
        return render(request, 'community/login.html', {'login_form': login_form})
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return redirect('home')


def register(request):
    return redirect('home')


def logout(request):
    return redirect('home')
