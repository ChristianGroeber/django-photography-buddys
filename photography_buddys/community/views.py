from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect


# Create your views here.
from .forms import PhotographerLoginForm, PhotographerCreationForm


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
    register_form = PhotographerCreationForm(request.POST or None)
    if request.method == 'GET':
        return render(request, 'community/login.html', {'register_form': register_form})
    if register_form.is_valid():
        print('valid')
        phot = register_form.save()
        photographers = Group.objects.get(name='Photographers')
        photographers.user_set.add(phot)
    return redirect('home')


def logout(request):
    return redirect('home')
