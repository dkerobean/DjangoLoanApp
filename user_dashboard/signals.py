from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile, SavingsAccount
from frontend.models import LoanApplication
from .utils import generate_account_number


@receiver(post_save, sender=User)
def createProfile(sender, created, instance, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create( # noqa
            user=user,
        )


@receiver(post_delete, sender=Profile)
def deleteProfile(sender, instance, **kwargs):
    user = instance.user
    user.delete()


@receiver(post_save, sender=User)
def create_accounts(sender, instance, created, **kwargs):
    if created:
        SavingsAccount.objects.create(user=instance,
                                      account_number=generate_account_number())
        LoanApplication.objects.create(user=instance, amount=0)
