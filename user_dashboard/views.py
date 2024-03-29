from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm, UpdateProfileForm
from .models import Profile, Support, Transaction, SavingsAccount, MessageReply
from frontend.models import LoanApplication
from django.contrib.auth.decorators import login_required
from .utils import generate_reference
from django.conf import settings
from django.db.models import Sum
from decimal import Decimal
from django.contrib.auth import get_user_model


@login_required(login_url="user-login")
def indexPage(request):

    user = request.user
    user_replies = MessageReply.objects.filter(support__user=user)

    # user = Profile.objects.get(id=pk)
    user_instance = request.user

    name = f"{request.user.first_name} {request.user.last_name}"
    username = request.user.username

    paystack_public_key = settings.PAYSTACK_PUBLIC_KEY

    # Paystack Deposit money
    if request.method == "POST":
        amount = int(request.POST['amount'])
        email = request.user.email
        transaction_type = 'Deposit'
        reference = generate_reference()
        user_id = request.user.id

        # create a Transaction
        transaction = Transaction.objects.create(
            user=user_instance, amount=amount,
            transaction_type=transaction_type, reference=reference)

        context = {
            'amount': amount,
            'email': email,
            'reference': reference,
            'paystack_public_key': paystack_public_key,
            'user_id': user_id,
            'transaction': transaction,
            'user_replies': user_replies
        }

        messages.warning(request, 'Proceed to make payment')
        return render(request, 'user_dashboard/confirm_payment.html', context)

    # Get all user transactions
    user_transactions = user_instance.transactions.all()[:4]

    # get user loan amount of approved loans
    approved_loans = LoanApplication.objects.filter(
        user=user_instance, status='approved')
    user_loan_amount = approved_loans.aggregate(Sum('amount'))['amount__sum']

    if user_loan_amount is None:
        user_loan_amount = 0.00

    # Get user available balance
    if user_loan_amount is not None:
        current_balance = user_instance.savings_account.balance \
                        - Decimal(user_loan_amount)
    else:
        current_balance = user_instance.savings_account.balance

    context = {
        'name': name,
        'username': username,
        'user_transactions': user_transactions,
        'user_loan_amount': user_loan_amount,
        'current_balance': current_balance
    }

    return render(request, 'user_dashboard/index.html', context)


""" AUTH """


user = get_user_model()
user.backend = 'django.contrib.auth.backends.ModelBackend'


def loginPage(request):

    if request.user.is_authenticated and request.user.is_staff:
        return redirect('admin-dashboard')
    elif request.user.is_authenticated:
        return redirect('user-home')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, 'Username does not exists')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            # user has staff status
            if user.is_staff:
                login(request, user)
                messages.success(request, 'Logged in succesfully')
                return redirect('admin-dashboard')

            # normal user without staff status
            login(request, user)
            messages.success(request, 'Logged in succesfully')

            return redirect(request.GET.get('next', 'user-home'))

        else:
            messages.error(request, 'Username or Password incorrect')

    return render(request, 'user_dashboard/auth/login.html')


def registerPage(request):

    form = CustomUserCreationForm()

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            messages.success(request, 'Account created successfuly')
            login(request, user)
            return redirect('user-home')

    context = {
        'form': form
    }

    return render(request, 'user_dashboard/auth/register.html', context)


@login_required(login_url="user-login")
def logout(request):

    auth_logout(request)
    messages.success(request, 'Logout Successfully')
    return redirect('index-page')

    return render(request, 'user_dashboard/auth/login.html')


""" PROFILE """


@login_required(login_url="user-login")
def edit_profile(request, pk):

    user_profile = Profile.objects.get(id=pk)
    name = f"{user_profile.user.first_name} {user_profile.user.last_name}"
    username = user_profile.user.username

    form = UpdateProfileForm(instance=user_profile)

    if request.method == "POST":
        form = UpdateProfileForm(request.POST, request.FILES,
                                 instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile Updated")
            return redirect('user-home')

    context = {
        'form': form,
        'name': name,
        'username': username
    }

    return render(request, 'user_dashboard/profile/edit_profile.html', context)


""" SUPPORT """


@login_required(login_url="user-login")
def support(request, pk):

    user = Profile.objects.get(id=pk)
    user_id = user.user.id
    user_instance = User.objects.get(id=user_id)

    name = f"{user.user.first_name} {user.user.last_name}"
    username = user.user.username

    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']

        support_ticket = Support.objects.create(user=user_instance,
                                                title=title,
                                                description=description)
        support_ticket.save()
        messages.success(request, 'Ticket submited successfully')
        return redirect('user-home')

    context = {
        'name': name,
        'username': username
    }

    return render(request, 'user_dashboard/support/support.html', context)


""" PAYSTACK """


@login_required(login_url="user-login")
def verifyPayment(request, reference, amount, status):

    transaction = Transaction.objects.get(reference=reference)

    user = request.user

    # Get users account
    user_account = SavingsAccount.objects.get(user=user)

    # Get amount paid
    amount_paid = amount

    if status == "False":
        messages.error(request, "Payment not verified")
        return redirect('user-home')
    else:
        transaction.verified = True

        # add amount paid to users accoubt balance
        user_account.balance += amount_paid
        user_account.save()

        transaction.save()
        messages.success(request, "Payment verified")
        return redirect('user-home')

    return render(request, 'user_dashboard/index.html')


""" TRANSACTIONS """


@login_required(login_url="user-login")
def showTransactions(request, pk):

    user = Profile.objects.get(id=pk)
    user_instance = request.user

    name = f"{user.user.first_name} {user.user.last_name}"
    username = user.user.username

    # Get all users transactions
    user_transactions = user_instance.transactions.all()

    context = {
        'user': user,
        'name': name,
        'username': username,
        'user_transactions': user_transactions
    }

    return render(
        request, 'user_dashboard/transactions/transaction.html', context
                  )


""" WALLET """


@login_required(login_url="user-login")
def myWallet(request, pk):

    user = Profile.objects.get(id=pk)
    user_instance = request.user

    name = f"{user.user.first_name} {user.user.last_name}"
    username = user.user.username

    # Get user acount balance
    user_account = SavingsAccount.objects.get(user=user_instance)

    # Get user transactions
    user_transactions = user_instance.transactions.all()[:5]

    # Paystack Deposit money

    paystack_public_key = settings.PAYSTACK_PUBLIC_KEY

    if request.method == "POST":
        amount = int(request.POST['amount'])
        email = user.user.email
        transaction_type = 'Deposit'
        reference = generate_reference()
        user_id = user.id

        # create a Transaction
        transaction = Transaction.objects.create(    # noqa
            user=user_instance, amount=amount,
            transaction_type=transaction_type, reference=reference)

        context = {
            'amount': amount,
            'email': email,
            'reference': reference,
            'paystack_public_key': paystack_public_key,
            'user_id': user_id
        }

        messages.warning(request, 'Proceed to make payment')
        return render(request, 'user_dashboard/confirm_payment.html', context)

    context = {
        'user': user,
        'name': name,
        'username': username,
        'user_account': user_account,
        'user_transactions': user_transactions,
    }

    return render(request, 'user_dashboard/wallet/wallet.html', context)


""" LOANS """


@login_required(login_url="user-login")
def userLoans(request, pk):

    user = Profile.objects.get(id=pk)
    user_instance = request.user

    name = f"{user.user.first_name} {user.user.last_name}"
    username = user.user.username

    # Get user's loan
    user_loan = user_instance.loans.all()

    context = {
        'user': user,
        'name': name,
        'username': username,
        'user_loan': user_loan
    }

    return render(request, 'user_dashboard/loans/loan.html', context)


""" INBOX """


def userInbox(request, pk):

    user = Profile.objects.get(id=pk)
    user_instance = request.user

    name = f"{user.user.first_name} {user.user.last_name}"
    username = user.user.username

    # get user messages
    user_messages = user_instance.support.all()

    all_replies = MessageReply.objects.all()

    context = {
        'user': user,
        'name': name,
        'username': username,
        'user_messages': user_messages,
        "all_replies": all_replies
    }

    return render(request, 'user_dashboard/inbox/inbox.html', context)
