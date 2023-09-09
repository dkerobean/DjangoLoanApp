from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages
from .models import LoanApplication
from django.contrib.auth.decorators import login_required


def indexPage(request):

    return render(request, 'frontend/index.html')


""" LOAN """


def getLoan(request):

    return render(request, 'frontend/loan/get_loan.html')


def loanApplication(request):

    return render(request, 'frontend/loan/loan_application')


@login_required(login_url="user-login")
def loanDetails(request):
    if request.method == "POST":
        loan_type = request.POST.get("select-loan-type")
        finance_type = request.POST.get("finance-type")
        loan_amount = request.POST.get("loan-amount")
        loan_duration = request.POST.get("loan-duration")

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


@login_required(login_url="user-login")
def personalDetails(request):

    if request.method == "POST":
        dob = request.POST.get('dob')
        marital_status = request.POST.get('marital-status')
        mobile_number = request.POST.get('mobile-number')
        address = request.POST.get('address')
        city = request.POST.get('city')
        postal_code = request.POST.get('postal-code')

        if dob and marital_status and \
           mobile_number and address and \
           city and postal_code:
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


@login_required(login_url="user-login")
def documentUpload(request):

    if request.method == "POST":

        id_proof = request.FILES.get('id-proof')

        # Get previous data from session
        loan_details = request.session.get('loan_details')
        personal_details = request.session.get('personal_details')

        if loan_details and personal_details:
            loan_application = LoanApplication(
                user=request.user,
                loan_type=loan_details['loan_type'],
                amount=loan_details['loan_amount'],
                duration=loan_details['loan_duration'],
                finance_type=loan_details['finance_type'],
                date_of_birth=personal_details['dob'],
                marital_status=personal_details['marital_status'],
                mobile_number=personal_details['mobile_number'],
                address=personal_details['address'],
                city=personal_details['city'],
                postal_code=personal_details['postal_code'],
                id_card=id_proof
            )

            loan_application.save()

            # Clear the session data
            del request.session['loan_details']
            del request.session['personal_details']

            messages.success(request, 'Loan Application submitted')

            return redirect('index-page')
        else:
            messages.error(request, "Please fill in all the required details.")

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
        'form': form
    }

    return render(request, 'frontend/contact.html', context)