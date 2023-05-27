from django.shortcuts import render, redirect
from .forms import ContactForm 
from django.contrib import messages



def indexPage(request):
    
    return render(request, 'frontend/index.html')

""" LOAN """

def getLoan(request):
    
    return render(request, 'frontend/loan/get_loan.html')


def loanApplication(request):
    
    return render(request, 'frontend/loan/loan_application')


def loanDetails(request):
    
    return render(request, 'frontend/loan/loan_details.html')


def personalDetails(request):
    
    return render(request, 'frontend/loan/personal_details.html')


def documentUpload(request):

    return render(request, 'frontend/loan/document_upload.html')


""" CONTACT """

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