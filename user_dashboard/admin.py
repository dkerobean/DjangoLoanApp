from django.contrib import admin
from .models import Profile, SavingsAccount, Loan, Transaction, Support

admin.site.register(Profile)
admin.site.register(SavingsAccount)
admin.site.register(Loan)
admin.site.register(Transaction)
admin.site.register(Support)
