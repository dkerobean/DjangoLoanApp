from django.shortcuts import render, redirect
from frontend.models import LoanApplication
from user_dashboard.models import SavingsAccount, Transaction
from django.db.models import Sum, Count
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test


#check if user is staff
def is_admin(user):
    return user.is_authenticated and user.is_staff


@login_required(login_url="user-login")
@user_passes_test(is_admin)
def indexPage(request):
    
    #total deposits for user
    total_deposit = SavingsAccount.objects.aggregate(Sum('balance'))[
        'balance__sum']
    formatted_deposit = "{:,.2f}".format(total_deposit)  # Format balance with commas
    
    #get sum of loans of users
    total_loans = LoanApplication.objects.filter(
        status='approved').aggregate(Sum('amount'))['amount__sum']
    formatted_loans = "{:,.2f}".format(total_loans)
    
    #get total users
    total_users = User.objects.count()
    
    #total loan application 
    number_of_loans = LoanApplication.objects.aggregate(total=Count('id'))['total']
    
    #all users transactions
    user_transactions = Transaction.objects.all()[:6]
    
    
    context = {
        'formatted_deposit':formatted_deposit,
        'formatted_loans':formatted_loans, 
        'total_users':total_users, 
        'number_of_loans': number_of_loans, 
        'user_transactions':user_transactions
    }
    
    return render(request, 'admin_dashboard/index.html', context)


@login_required(login_url="user-login")
@user_passes_test(is_admin)
def loanApplicants(request):
    
    all_loans = LoanApplication.objects.all()
    
    context = {
        'all_loans':all_loans,
    }
    
    return render(request, 'admin_dashboard/loan_applicants/all_loans.html', context)


@login_required(login_url="user-login")
@user_passes_test(is_admin)
def viewApplication(request, pk):
    
    user_loan = LoanApplication.objects.get(id=pk)
    
    if request.method == 'POST':
        loan_status = request.POST.get('status')
        user_loan.status = loan_status
        user_loan.save()
        messages.success(request, 'Status Changed successfully')
        return redirect('all-loans')
        
        
    context = {
        'user_loan':user_loan
    }
    
    return render(request, 'admin_dashboard/loan_applicants/view_loan.html', context)


@login_required(login_url="user-login")
@user_passes_test(is_admin)
def viewTransactions(request):
    
    all_transactions = Transaction.objects.all()
    
    context = {
        'all_transactions':all_transactions
    }
    
    return render(request, 'admin_dashboard/transactions/view.html', context)
