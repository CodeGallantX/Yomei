from django.shortcuts import render, redirect
from .models import Transaction
from .forms import TransactionForm

# Create your views here.
def transaction_list(request):
    transactions = Transaction.objects.all().order_by('-timestamp')[:5]
    return render(request, 'transactions/transaction_list_.html', {'transactions':transactions})

def make_transaction(request):
    if request.method  == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return
        redirect('transaction_list')
    else:
        form = TransactionForm()
        return render(request, 'transactions/make_transactions.html', {'form':form})