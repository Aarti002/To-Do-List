from django import forms
from django.contrib.auth.models import User
from django.forms import widgets
from .models import *
import json



class DateInput(forms.DateInput):
    input_type = 'date'


class UserLoginForm(forms.ModelForm):
    email = forms.CharField(
                            widget=forms.TextInput(attrs={'id': 'email', 'class': 'form-control mb-3'}),
                            required=True)
    password = forms.CharField(
                            widget=forms.PasswordInput(attrs={'id': 'password', 'class': 'form-control mb-3'}),
                            required=True)


    class Meta:
        model=User
        fields=['email','password']


