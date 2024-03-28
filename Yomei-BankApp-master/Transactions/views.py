from django.shortcuts import render, redirect
from .models import Transaction
from .forms import TransactionForm
from django.contrib import messages


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

def transfer_funds(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            # Process the form data and perform the transfer operation
            user_account = form.cleaned_data['user_account']
            recipient_account = form.cleaned_data['recipient_account']
            amount = form.cleaned_data['amount']
            recipient_bank_name = form.cleaned_data['recipient_bank_name']
            
            # Assuming you have the sender and recipient objects based on their account numbers
            sender_wallet = Wallet.objects.get(account_number=user_account)
            recipient_wallet = Wallet.objects.get(account_number=recipient_account)

            # Check if sender has enough balance
            if sender_wallet.balance >= amount:
                # Deduct amount from sender's wallet
                sender_wallet.balance -= amount
                sender_wallet.save()

                # Add amount to recipient's wallet
                recipient_wallet.balance += amount
                recipient_wallet.save()

                # Record the transaction
                Transaction.objects.create(sender=sender_wallet.user, recipient=recipient_wallet.user, amount=amount)

                messages.success(request, 'Transfer successful!')
                return redirect('transactions')  # Redirect to transactions page after successful transfer
            else:
                messages.error(request, 'Insufficient balance.')
    else:
        form = TransferForm()
    
    return render(request, 'transactions.html', {'form': form})

def payment(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Withdrawal successful')
            return redirect('dashboard')  # Redirect to the dashboard page
    else:
        form = TransactionForm()
    return render(request, 'InfinityFinance/dashboard', {'form': form})

# Similarly, implement views for other transaction operations like transfer, payment, etc.
