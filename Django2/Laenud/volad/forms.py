from django import forms
from django.contrib.auth.models import User
from .models import Debt
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.apps import apps
Debt = apps.get_model('volad', 'Debt')

class DebtForm(forms.ModelForm):
    class Meta:
        model = Debt
        fields = ['creditor', 'debtor', 'amount', 'notes']
        labels = {
            'creditor': 'Who do you owe?',
            'debtor': 'Who owes the money?',
            'amount': 'How much?',
            'notes': 'Any notes?'
        }
        help_texts = {
            'creditor': 'Select a user from the list.',
            'debtor': 'Select a user from the list.',
            'amount': 'Enter a positive number.',
            'notes': 'Optional. You can write anything here.'
        }

class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')