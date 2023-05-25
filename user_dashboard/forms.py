from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm



class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User 
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update(
                {'class': 'text-bgray-800 text-base border border-bgray-300 h-14 w-full focus:border-success-300 focus:ring-0 rounded-lg px-4 py-3.5 placeholder:text-bgray-500 placeholder:text-base', 
                 'placeholder':field.label})
            
            
class UpdateProfileForm(ModelForm):
    
    class Meta:
        model = Profile 
        fields = '__all__'
        exclude = ('user',)
        
        
    def __init__(self, *args, **kwargs):
        super(UpdateProfileForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update(
                {'class': 'bg-bgray-50 p-4 rounded-lg h-14 border-0 focus:border focus:border-success-300 focus:ring-0',
                 'placeholder':field.label})
        
        
