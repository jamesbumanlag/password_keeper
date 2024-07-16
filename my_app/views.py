from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import SignUpForm


def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        messages.success(request,'Not Authorized')
        return redirect('login')

def reset(request):
    return render(request, 'reset.html')


def register(request):
    
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()

            # Authenticate
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request,user)
            messages.success(request,'Logged in Successfully')
            return redirect('home')
        else:
            messages.success(request,'Login Failed')
            return render (request, 'login.html',{'form':form})
    else:
        form = SignUpForm() 
        return render(request, 'register.html', {'form':form})


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