from django.http import HttpResponse, HttpRequest
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.db import IntegrityError

# Create your views here.



def register(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                login(request, user)
                return redirect('home')  # Redirect to your home page
            except IntegrityError:
                form.add_error('username', 'This username is already taken.')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})


def user_login(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to your home page
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

def user_logout(request: HttpRequest) -> HttpResponse:
    logout(request)
    return redirect('home')  # Redirect to your home page

def home(request):
    # Your view logic here
    return render(request, 'home.html')