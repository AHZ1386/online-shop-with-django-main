import re
from django import forms
from .models import User,Otp
from django.contrib.auth.forms import UserCreationForm
from phonenumber_field.formfields import PhoneNumberField
import phonenumbers

class UserCreateForm(UserCreationForm):


    class Meta:
        model = User
        fields = ['phone_number', 'password1', 'password2']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['phone_number', 'first_name','last_name','address',]


class OtpForm(forms.ModelForm):
    class Meta:
        model = Otp
        fields = ['otp']