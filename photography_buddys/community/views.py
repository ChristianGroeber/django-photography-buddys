from django.shortcuts import render, redirect


# Create your views here.


def index(request):
    return redirect('home')


def login(request):
    return redirect('home')


def register(request):
    return redirect('home')


def logout(request):
    return redirect('home')
