from django.shortcuts import render, redirect
from .forms import ContactForm 
from django.contrib import messages



def indexPage(request):
    
    return render(request, 'frontend/index.html')


def getLoan(request):
    
    return render(request, 'frontend/get_loan.html')


def loanApplication(request):
    
    return render(request, 'frontend/loan_application')

from django.contrib import messages

def contact(request):
    
    form = ContactForm()
    
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Message Sent!')
            return redirect('index-page')
        
    context = {
        'form':form
    }
    
    return render(request, 'frontend/contact.html', context)