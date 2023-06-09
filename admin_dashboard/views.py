from django.shortcuts import render
from frontend.models import LoanApplication
from .forms import LoanForm

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
    
    form = LoanForm()
    
    if request.method == "POST":
        form = LoanForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Status changed successfully')
            return redirect('all-loans')
            
    
    context = {
        'user_loan':user_loan, 
        'form':form
    }
    
    return render(request, 'admin_dashboard/loan_applicants/view_loan.html', context)
