from django.forms import ModelForm
from user_dashboard.models import Profile
from django import forms


class UpdateProfileForm(ModelForm):
    first_name = forms.CharField(max_length=100, required=False)
    last_name = forms.CharField(max_length=100, required=False)
    username = forms.CharField(max_length=100, required=False)
    email = forms.EmailField(required=False)

    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ('user',)

    # Overide init method to include  some fields from user model
    def __init__(self, *args, **kwargs):
        super(UpdateProfileForm, self).__init__(*args, **kwargs)
        user_instance = self.instance.user

        if user_instance:
            self.fields['first_name'].initial = user_instance.first_name
            self.fields['last_name'].initial = user_instance.last_name
            self.fields['username'].initial = user_instance.username
            self.fields['email'].initial = user_instance.email

        for name, field in self.fields.items():
            field.widget.attrs.update(
                {'class': 'bg-bgray-50 p-4 \
                 rounded-lg h-14 border-0 \
                 focus:border focus:border-success-300 focus:ring-0',
                 'placeholder': field.label})

    # Save first and last name, usename and email from User model
    def save(self, commit=True):
        instance = super().save(commit=False)
        user_instance = instance.user

        if user_instance:
            if self.is_valid():
                user_instance.first_name = self.cleaned_data['first_name']
                user_instance.last_name = self.cleaned_data['last_name']
                user_instance.username = self.cleaned_data['username']
                user_instance.email = self.cleaned_data['email']
                user_instance.save()

        if commit:
            instance.save()

        return instance
