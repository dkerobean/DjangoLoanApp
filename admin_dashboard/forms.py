from django.forms import ModelForm
from frontend.models import LoanApplication


class LoanForm(ModelForm):
    class Meta:
        model = LoanApplication
        fields = ['status']

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.status = self.cleaned_data['status']

        if commit:
            instance.save()

        return instance




        
