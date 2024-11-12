from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect


def home_view(request):
    return render(request, 'backend/home.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to a home or profile page
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'backend/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page


@csrf_protect
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('login')
        else:
            messages.error(request, 'Registration failed. Try again.')
    else:
        form = UserCreationForm()
    return render(request, 'backend/register.html', {'form': form})


@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html')
