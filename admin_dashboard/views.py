from django.shortcuts import render

def indexPage(request):
    
    return render(request, 'admin_dashboard/index.html')