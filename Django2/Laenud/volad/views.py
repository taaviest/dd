from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Debt
from .forms import DebtForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Debt
from .forms import DebtForm
from .forms import LoginForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import SignUpForm
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# Create your views here.
@login_required
def create_debt(request):
    if request.method == 'POST':
        form = DebtForm(request.POST)
        if form.is_valid():
            debt = form.save(commit=False)
            debt.save()
            return redirect('debt_list')
    else:
        form = DebtForm()
    return render(request, 'create_debt.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'You have successfully logged in.')
                return redirect('debt_list')
            else:
                form.add_error(None, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def debt_list(request):
    debts = Debt.objects.filter(user=request.user)
    return render(request, 'debt_list.html', {'debts': debts})

@login_required
def create_debt(request):
    if request.method == 'POST':
        form = DebtForm(request.POST)
        if form.is_valid():
            debt = form.save(commit=False)
            debt.user = request.user
            debt.save()
            return redirect('debt_list')
    else:
        form = DebtForm()
    return render(request, 'create_debt.html', {'form': form})

@login_required
def update_debt(request, pk):
    debt = get_object_or_404(Debt, pk=pk, user=request.user)
    if request.method == 'POST':
        form = DebtForm(request.POST, instance=debt)
        if form.is_valid():
            form.save()
            return redirect('debt_list')
    else:
        form = DebtForm(instance=debt)
    return render(request, 'update_debt.html', {'form': form})

@login_required
def delete_debt(request, pk):
    debt = get_object_or_404(Debt, pk=pk, user=request.user)
    if request.method == 'POST':
        debt.delete()
        return redirect('debt_list')
    return render(request, 'delete_debt.html', {'debt': debt})

class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()