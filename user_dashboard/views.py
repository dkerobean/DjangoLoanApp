from django.shortcuts import render


""" AUTH """
def loginPage(request):
    
    return render(request, 'user_dashboard/auth/login.html')


def registerPage(request):
    
    return render(request, 'user_dashboard/auth/register.html')