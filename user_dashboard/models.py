from django.db import models
import uuid
from django.contrib.auth.models import User
from .utils import generate_account_number
from frontend.models import LoanApplication


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True,
        related_name='profile')
    date_of_birth = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/',
                                        blank=True, null=True,
                                        default="profile_pictures/avatar.svg")
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.user.username


class SavingsAccount(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='savings_account')
    account_number = models.CharField(
        max_length=10, default=generate_account_number)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2,
                                        blank=True, null=True)

    def __str__(self):
        return f"{self.user} - {self.account_number}"


class Transaction(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='transactions')
    # account = models.ForeignKey(
    #     SavingsAccount, on_delete=models.CASCADE,
    #     blank=True, null=True,
#         related_name='transactions')
    loan = models.ForeignKey(LoanApplication, on_delete=models.CASCADE,
                             blank=True, null=True,
                             related_name='transactions')
    transaction_type = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    reference = models.CharField(max_length=255, blank=True, null=True)
    verified = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return f"{self.transaction_type} - {self.amount}"

    class Meta:
        ordering = ['-timestamp']


class Support(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='support')
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.title


class MessageReply(models.Model):
    support = models.ForeignKey(
        Support, on_delete=models.CASCADE, related_name='replies')
    reply_content = models.CharField(max_length=250)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f"Reply to: {self.support.title}"
