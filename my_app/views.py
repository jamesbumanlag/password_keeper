from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import *
from .models import *


def home(request):
    if request.user.is_authenticated:
        accounts = PersonAccount.objects.all()
        return render(request, 'home.html',{'accounts':accounts})
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
            messages.success(request,'Invalid Input')
            return render (request, 'login.html',{'form':form})
    else:
        form = SignUpForm() 
        return render(request, 'register.html', {'form':form})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

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


def add(request):
    if request.user.is_authenticated:
        person_form = PersonAccountModelForm(request.POST or None)
        if request.method == 'POST':
            if person_form.is_valid():
                person_form.save()
                messages.success(request, 'Record Saved')
                return redirect('home')
            else:
                person_form = PersonAccountModelForm()
                messages.success(request, 'Error! Invalid Input')
                return render(request,'add_account.html', {'person_form':person_form})
        return render(request,'add_account.html', {'person_form':person_form})
    else:
        
        messages.success(request,'Invalid Access')
        return redirect('login')