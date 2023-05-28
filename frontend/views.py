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
    if request.method == "POST":
        loan_type = request.POST["select-loan-type"]
        finance_type = request.POST["finance-type"]
        loan_amount = request.POST["loan-amount"]
        loan_duration = request.POST["loan-duration"]

        if loan_type and finance_type and loan_amount and loan_duration:
            request.session['loan_details'] = {
                'loan_type': loan_type,
                'finance_type': finance_type,
                'loan_amount': loan_amount,
                'loan_duration': loan_duration
            }
            return redirect('personal-details')
        else:
            messages.error(request, "Please fill in all the fields.")
            

    return render(request, 'frontend/loan/loan_details.html')



def personalDetails(request):
    
    if request.method == "POST":
        dob = request.POST['dob']
        marital_status = request.POST['marital-status']
        mobile_number = request.POST['mobile-number']
        address = request.POST['address']
        city = request.POST['city']
        postal_code = request.POST['postal-code']
        
        if dob and marital_status and mobile_number and address and city and postal_code:
            request.session['personal_details'] = {
                'dob': dob,
                'marital_status': marital_status,
                'mobile_number': mobile_number, 
                'address': address,
                'city': city,
                'postal_code': postal_code
            }
            return redirect('document-upload')
        
        else:
            messages.error(request, "Please fill in all the fields.")
    
    return render(request, 'frontend/loan/personal_details.html')


def documentUpload(request):
    
    if request.method == "POST":
        id_proof = request.FILES['id-proof']
        
        if id_proof:
            request.session['document_upload'] = {
                'id_proof': id_proof
            }
            
            
        else:
            messages.error(request, "Please upload id proof.")

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