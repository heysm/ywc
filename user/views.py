from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout
# Create your views here.


def signupuser(request):
    if request.method == "GET":
        return render(request, 'user/signup.html', {"form": UserCreationForm()})
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('user:dashboard')

            except IntegrityError:
                return render(request, 'user/signup.html', {"form": UserCreationForm(), "error": "Username Chosen has already been taken"})
        else:
            return render(request, 'user/signup.html', {"form": UserCreationForm(), "error": "Your password1 and 2 didnot match"})


def dashboard(request):
    return render(request, 'user/dashboard.html')


def logoutuser(request):
    if request.method == "POST":
        logout(request)
        return redirect('home:home')
