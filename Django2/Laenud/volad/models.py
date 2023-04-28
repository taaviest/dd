from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Debt(models.Model):
    debtor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='debts')
    creditor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='credits')
    amount = models.DecimalField(max_digits=10, decimal_places=2)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)