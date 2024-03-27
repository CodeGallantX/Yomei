from django.shortcuts import render, redirect
from .models import Transaction
from .forms import TransactionForm

# Create your views here.
def transaction_list(request):
    transactions = Transaction.objects.all().order_by('-timestamp')