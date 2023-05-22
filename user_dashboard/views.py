from django.shortcuts import render


""" AUTH """
def loginPage(request):
    
    return render(request, 'user_dashboard/index.html')
