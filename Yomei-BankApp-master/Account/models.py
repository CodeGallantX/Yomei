from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_number = models.CharField(max_length = 20, unique=True)
    balance = models.DecimalField(max_digits = 10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.user.username}'s Wallet"