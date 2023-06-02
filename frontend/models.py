from django.db import models
from django.contrib.auth.models import User
import uuid



class Contact(models.Model):
    
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    subject = models.CharField(max_length=150)
    message = models.TextField(max_length=500)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    
    def __str__(self):
        return self.name
    

class LoanApplication(models.Model):
    
    LOAN_STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )
    
    LOAN_FINANCE_TYPE = (
        ('credit', 'Credit'), 
        ('debt', 'Debt'),
    )
    
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='loans')
    loan_type = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    outstanding_balance = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)
    duration = models.IntegerField()
    finance_type = models.CharField(
        max_length=20, choices=LOAN_FINANCE_TYPE, default='credit')
    interest_rate = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    date_of_birth = models.DateField()
    marital_status = models.CharField(max_length=50)
    mobile_number = models.IntegerField()
    address = models.CharField(max_length=50)
    country = models.CharField(max_length=150)
    city = models.CharField(max_length=50)
    postal_code = models.IntegerField()
    id_card = models.ImageField(upload_to='ids/', null=True, blank=True)
    status = models.CharField(max_length=20, choices=LOAN_STATUS_CHOICES, default='pending') 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                         primary_key=True, editable=False)
    
    def __str__(self):
        return f"Loan Application - {self.user.username}"
    
    