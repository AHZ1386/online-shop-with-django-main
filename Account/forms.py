import re
from django import forms
from .models import User,Otp
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2','phone_number']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name','last_name','phone_number','address',]


class OtpForm(forms.ModelForm):
    class Meta:
        model = Otp
        fields = ['otp']