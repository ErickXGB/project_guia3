from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import UserRegisterForm, UserLoginForm

def signup_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = UserRegisterForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('home')
    return render(request, 'authentication/signup.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = UserLoginForm(request, data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.get_user()
        login(request, user)
        next_url = request.GET.get('next')
        if next_url:
            return redirect(next_url)
        return redirect('home')
    return render(request, 'authentication/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')
