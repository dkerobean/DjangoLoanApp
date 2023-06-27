from django.shortcuts import render, redirect
from frontend.models import LoanApplication
from user_dashboard.models import SavingsAccount, Transaction, Profile, Support, MessageReply
from django.db.models import Sum, Count
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from .forms import UpdateProfileForm


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
    total_loans = LoanApplication.objects.filter(status='approved').aggregate(Sum('amount'))['amount__sum']
    formatted_loans = "{:,.2f}".format(total_loans) if total_loans is not None else "0.00"

    
    #get total users
    total_users = User.objects.count()
    
    #total loan application 
    number_of_loans = LoanApplication.objects.aggregate(total=Count('id'))['total']
    
    #all users transactions
    user_transactions = Transaction.objects.all()[:6]
    
    #get user messages 
    all_messages = Support.objects.all()
    
    
    context = {
        'formatted_deposit':formatted_deposit,
        'formatted_loans':formatted_loans, 
        'total_users':total_users, 
        'number_of_loans': number_of_loans, 
        'user_transactions':user_transactions, 
        "all_messages": all_messages
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


@login_required(login_url="user-login")
@user_passes_test(is_admin)
def editProfile(request, pk):
    
    user_profile = Profile.objects.get(id=pk)

    form = UpdateProfileForm(instance=user_profile)

    if request.method == "POST":
        form = UpdateProfileForm(
            request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile Updated")
            return redirect('admin-dashboard')

    context = {
        'form': form
    }
    
    
    return render(request, 'admin_dashboard/profile/edit.html', context)


@login_required(login_url="user-login")
@user_passes_test(is_admin)
def inbox(request):
    
    all_messages = Support.objects.all()
    
    context = {
        'all_messages':all_messages
    }
    
    return render(request, 'admin_dashboard/inbox/all.html', context)


@login_required(login_url="user-login")
@user_passes_test(is_admin)
def viewMessage(request, pk):
    
    message = Support.objects.get(id=pk)
    all_messages = Support.objects.all()
    
    all_replies = MessageReply.objects.all()
    
    #save reply to user message
    if request.method == "POST":
        reply = request.POST.get('reply')
        message_reply = MessageReply(support=message, reply_content=reply)
        message_reply.save()
        messages.success(request, 'Reply Sent')
        return redirect('admin-inbox-read', message.id)
        
    
    context = {
        'message':message, 
        'all_messages':all_messages, 
        'all_replies':all_replies
    }
    
    return render(request, 'admin_dashboard/inbox/view.html', context)
