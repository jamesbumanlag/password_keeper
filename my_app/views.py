from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def reset(request):
    return render(request, 'reset.html')


def register(request):
    return render(request, 'register.html')


def login_user(request):
    return render(request, 'login.html')