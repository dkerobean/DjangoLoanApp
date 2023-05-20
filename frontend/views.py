from django.shortcuts import render



def indexPage(request):
    
    return render(request, 'frontend/index.html')


def getLoan(request):
    
    return render(request, 'frontend/get_loan.html')


def loanApplication(request):
    
    return render(request, 'frontend/loan_application')


def contact(request):
    
    return render(request, 'frontend/contact.html')