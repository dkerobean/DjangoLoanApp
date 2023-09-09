from django.contrib import admin
from .models import Profile, SavingsAccount, Transaction, Support

admin.site.register(Profile)
admin.site.register(SavingsAccount)
admin.site.register(Transaction)
admin.site.register(Support)
# admin.site.register(SupportReply)
