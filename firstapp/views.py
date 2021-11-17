from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import SignUpForm
def signupview(request):
    form = SignUpForm() #blank
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'signup.html', {'form':form})

def loginview(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect ('loginsuccess')
        messages.error(request, 'Wrong Credentials!')
    return render(request, 'login.html')

def loginsuccess(request):
    return render(request, 'loginsuccess.html')

def logoutview(request):
    logout(request)
    return redirect('login')