import re
from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name','last_name','phone_number','address',]
