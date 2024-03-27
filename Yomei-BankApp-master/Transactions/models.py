from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_number = models.CharField(max_length = 20, unique=True)
    balance = models.DecimalField(max_digits = 10, decimal_places=2)

    def __str__(self):
        return f"{self.user.username}'s Wallet"

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
        db_table = 'transactions'

    def __str__(self):
        return f"{self.trans_type} - {self.amount}"