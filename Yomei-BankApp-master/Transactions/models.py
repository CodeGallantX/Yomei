from django.db import models
from Account.models import Account

# Create your models here.
class Transaction(models.Model):
    TRANS_TYPE_CHOICES = (
       ('deposit', 'Deposit'),
       ('withdrawal', 'Withdrawal'),
       ('transfer', 'Transfer'),
       ('payment', 'Payment'),
       ('other', 'Other'),
    )

    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.DecimalField(max_)
    type = models.CharField(max_length=30)
    trans_type = models.CharField(max_length=20, choices=TRANS_TYPE_CHOICES)
    timestamp = models.DateTimeField(add_now_add=True)
    description = models.CharField(max_length=255, blank=True)
    
    class Meta:
        db_table = 'transactions'

    def __str__(self):
        return f"{self.trans_type} - {self.amount}"

    @staticmethod
    def get_recent_transactions(account, num_transactions=5):
        return Transaction.objects.filter(account=account).order_by('-timestamp')[:num_transactions]