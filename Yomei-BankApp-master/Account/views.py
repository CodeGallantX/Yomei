from django.shortcuts import render
from Transactions.models import Transaction
from .models import Account

# Create your views here.
def account_detail(request, account_number):
    account = Account.objects.get(account_number = account_number)

    transactions = Transaction.objects.filter(account = account)
    return render(request, 'account/account_detail.html', {'account':account,
                                                           'transactions':transactions})        