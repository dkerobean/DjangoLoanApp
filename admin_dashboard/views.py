from django.shortcuts import render
from frontend.models import LoanApplication 

def indexPage(request):
    
    return render(request, 'admin_dashboard/index.html')


def loanApplicants(request):
    
    all_loans = LoanApplication.objects.all()
    
    context = {
        'all_loans':all_loans,
    }
    
    return render(request, 'admin_dashboard/loan_applicants/all_loans.html', context)


def viewApplication(request, pk):
    
    user_loan = LoanApplication.objects.get(id=pk)
    
    context = {
        'user_loan':user_loan
    }
    
    return render(request, 'admin_dashboard/loan_applicants/view_loan.html', context)
