from django.shortcuts import render, redirect
from .models import Transaction
from .forms import TransactionForm


# Create your views here.
def transaction_list(request):
    transactions = Transaction.objects.all().order_by('-timestamp')[:5]
    return render(request, 'InfinityFinance/dashboard.html', {'transactions':transactions})

def make_transaction(request):
    if request.method  == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return
        redirect('InfinityFinance/dashboard.html')
    else:
        form = TransactionForm()
        return render(request, 'InfinityFinance/dashboard.html', {'form':form})

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Transaction
from .forms import TransactionForm

def deposit(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Deposit successful')
            return redirect('dashboard')  # Redirect to the dashboard page
    else:
        form = TransactionForm()
    return render(request, 'InfinityFinance/deposit.html', {'form': form})

def withdrawal(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Withdrawal successful')
            return redirect('dashboard')  # Redirect to the dashboard page
    else:
        form = TransactionForm()
    return render(request, 'InfinityFinance/withdrawal.html', {'form': form})

# Similarly, implement views for other transaction operations like transfer, payment, etc.

def transfer(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Deposit successful')
            return redirect('dashboard')  # Redirect to the dashboard page
    else:
        form = TransactionForm()
    return render(request, 'InfinityFinance/deposit.html', {'form': form})

def payment(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Withdrawal successful')
            return redirect('dashboard')  # Redirect to the dashboard page
    else:
        form = TransactionForm()
    return render(request, 'InfinityFinance/withdrawal.html', {'form': form})

# Similarly, implement views for other transaction operations like transfer, payment, etc.
