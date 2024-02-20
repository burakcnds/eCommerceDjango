from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import *


def account(request):
    if request.method == 'POST':
        if 'signup' in request.POST:
            register_form = SignUpForm(request.POST)
            if register_form.is_valid():
                user = register_form.save()
                login(request, user)
                return redirect('index')
        elif 'login' in request.POST:
            login_form = LoginForm(request, request.POST)
            if login_form.is_valid():
                user = login_form.get_user()
                login(request, user)
                return redirect('index')
    else:
        register_form = UserCreationForm()
        login_form = AuthenticationForm()

    return render(request, 'account.html', {'register_form': register_form, 'login_form': login_form})

def profile(request):
    return render(request,'profile.html')

def userLogout(request):
    logout(request)
    return redirect('index')