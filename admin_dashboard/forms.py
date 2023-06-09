from django.forms import ModelForm
from frontend.models import LoanApplication


class LoanForm(ModelForm):
    class Meta:
        model = LoanApplication
        fields = ['status']

    def __init__(self, *args, **kwargs):
        super(LoanForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update(
                {'class': 'text-bgray-800 text-base border border-bgray-300 h-14 w-full focus:border-success-300 focus:ring-0 rounded-lg px-4 py-3.5 placeholder:text-bgray-500 placeholder:text-base',
                 'placeholder': field.label})

    def save(self, commit=True):
        instance = super(LoanForm, self).save(commit=False)

        # Set the 'status' field value directly on the instance
        instance.status = self.cleaned_data['status']

        if commit:
            instance.save()

        return instance


    

