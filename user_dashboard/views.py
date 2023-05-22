from django.shortcuts import render, redirect 
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm


def indexPage(request):
    
    return render(request, 'user_dashboard/index.html')

 
""" AUTH """

def loginPage(request):
    
    if request.user.is_authenticated:
        return redirect('user-home')
    
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exists')
            
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in succesfully')
            return redirect('user-home')
        else:
            messages.error(request, 'Username or Password incorrect')
            
    
    return render(request, 'user_dashboard/auth/login.html')


def registerPage(request):
    
    form = CustomUserCreationForm()
    
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            messages.success(request, 'Account created successfuly')
            login(request, user)
            return redirect('user-home')
        
    context = {
        'form':form
    }
    
    return render(request, 'user_dashboard/auth/register.html', context)


def logout(request):
    
    auth_logout(request)
    return redirect('index-page')
    
    return render(request, 'user_dashboard/auth/login.html')
