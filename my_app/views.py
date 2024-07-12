from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect


def home(request):
    return render(request, 'home.html')

def reset(request):
    return render(request, 'reset.html')


def register(request):
    return render(request, 'register.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['username']

        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login Successfully')
            return redirect('home')
        else:
            messages.success(request, 'Invalid Credentials')
            return render(request, 'login.html')

    else:
        return render(request, 'login.html')
    


def logout_user(request):
    logout(request)
    return redirect('login')