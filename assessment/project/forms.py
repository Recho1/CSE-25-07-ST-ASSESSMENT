from django import forms
from django.core.exceptions import ValidationErro

from django import forms
from project.models import Signup  

class SignupForm(forms.Form):
    fullname = forms.CharField(max_length=100)
    email = forms.EmailField()
    phonenumber = forms.CharField(max_length=15)
    password = forms.CharField(max_length=8, widget=forms.PasswordInput)
    confirm_password = forms.CharField(max_length=8, widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        
        if password and confirm_password and password != confirm_password:
            
            self.add_error("confirm_password", "")
        return cleaned_data
