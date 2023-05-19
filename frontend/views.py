from django.shortcuts import render



def indexPage(request):
    
    return render(request, 'frontend/index.html')