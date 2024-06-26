from django.db import models
from django.contrib.auth.models import User
import random

# Create models here

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)

class UserBankAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=20, unique=True)

class AccountData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=20, unique=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)


class Account(models.Model):
    account_number = models.CharField(max_length=100)
      
    def __str__(self):
        return self.account_number
    # Add other methods as needed

class NewAccount(Account):
    def __init__(self, customer_obj):
        new_acc = AccountData()
        new_acc.account_number = randomGen()
        new_acc.balance = 0
        new_acc.user = customer_obj.user
        new_acc.save()
        super().__init__(new_acc)

# Adjust other classes and methods similarly

class Transaction(models.Model):
    TRANS_TYPE_CHOICES = (
       ('deposit', 'Deposit'),
       ('withdrawal', 'Withdrawal'),
       ('transfer', 'Transfer'),
       ('payment', 'Payment'),
       ('other', 'Other'),
    )

    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    trans_type = models.CharField(max_length=20, choices=TRANS_TYPE_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=255, blank=True)
    
    class Meta:
        db_table = 'accounts'

    def __str__(self):
        return f"{self.trans_type} - {self.amount}"
    
    