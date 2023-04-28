from django import forms
from django.contrib.auth.models import User
from .models import Debt
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm

class DebtForm(forms.ModelForm):
    class Meta:
        model = Debt
        fields = ['debtor', 'creditor', 'amount']

def LoginForm(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # Log the user in.
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

class LoginForm(AuthenticationForm):
    pass

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')