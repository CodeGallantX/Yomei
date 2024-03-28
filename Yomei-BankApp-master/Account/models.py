from django.db import models
from django.contrib.auth.models import User
import random
from Transactions.models import Transaction

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    # Add other fields as needed

class UserBankAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=20, unique=True)
    # Add other fields as needed

class AccountData(models.Model):  # Renamed to avoid conflicts
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=20, unique=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    # Add other fields as needed

# Adjust other models as needed

class Account:
    def __init__(self, account_data):
        self.account_number = account_data.account_number
        self.account_data = account_data
        self.transactions = {}

        transaction_list = Transaction.objects.filter(account_number=account_data)
        for trans in transaction_list:
            self.transactions[trans.id] = Transaction(trans)

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



