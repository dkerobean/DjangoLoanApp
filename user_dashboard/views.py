from django.shortcuts import render, redirect 
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm, UpdateProfileForm
from .models import Profile
from django.contrib import messages


def indexPage(request, pk):
    
    user = Profile.objects.get(id=pk)
    
    name = f"{user.user.first_name} {user.user.last_name}"
    username = user.user.username
    
    context = {
        
        'user':user, 
        'name':name,
        'username':username
    }
    
    return render(request, 'user_dashboard/index.html', context)

 
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
            user_id = request.user.profile.id
            return redirect('user-home', user_id)
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


""" PROFILE """

def edit_profile(request, pk):
    
    user_profile = Profile.objects.get(id=pk)
    name = f"{user_profile.user.first_name} {user_profile.user.last_name}"
    username = user_profile.user.username
    
    form = UpdateProfileForm(instance=user_profile)
    
    if request.method == "POST":
        form = UpdateProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile Updated")
            user_id = request.user.profile.id
            return redirect('user-home', user_id)
        
        
    context = {
        'form':form,
        'name':name, 
        'username':username
    }
            
    
    return render(request, 'user_dashboard/profile/edit_profile.html', context)
