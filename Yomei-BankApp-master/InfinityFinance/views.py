from sqlite3 import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404


from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.http import HttpResponse
from Transactions.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.core.mail import EmailMessage, get_connection
import random


def home(request):
    return render(request, 'InfinityFinance/homepage.html')

def error_404(request, exception):
    return render(request, 'InfinityFinance/404.html', status=404)


'''
def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to login page or dashboard after successful registration
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'InfinityFinance/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully logged in!')
            return redirect('dashboard')  # Redirect to account details page
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')'''



def dashboard(request):
    user = request.user
    recent_transactions = Transaction.objects.order_by('-timestamp')[:5]

    transactions = Transaction.objects.filter(wallet=wallet)
    #bills = Bill.objects.filter(user=user)
    #airtime_purchases = AirtimePurchase.objects.filter(user=user)

    try:
        wallet = Wallet.objects.get(user=user)
    except Wallet.DoesNotExist:
        # Create a new wallet if it doesn't exist for the user
        wallet = Wallet.objects.create(user=user, account_number="3018725946")  # You may generate a unique account number here
    context = {
        'wallet': wallet,
        'recent_transactions':recent_transactions,
        'transaction': transactions,
        #'bills': bills,
        #'airtime_purchases': airtime_purchases
    }
    return render(request, 'InfinityFinance/dashboard.html', context)

'''
def transfer(request):
    # Implement money transfer logic here
    return render(request, 'InfinityFinance/transfer.html')

def pay_bill(request):
    # Implement bill payment logic here
    return render(request, 'bills.html')

def buy_airtime(request):
    # Implement airtime purchase logic here
    return render(request, 'buy-airtime.html')'''

def contact(request):
    return render(request, 'InfinityFinance/contact.html')

def thank_you(request):
    return render(request, 'InfinityFinance/thank_you.html')

def blog(request):
    return render(request, "InfinityFinance/blog.html")

def pricing(request):
    return render(request, "InfinityFinance/pricing.html")

def send_email(request):  
   if request.method == "POST": 
       with get_connection(  
           host=settings.EMAIL_HOST, 
     port=settings.EMAIL_PORT,  
     username=settings.EMAIL_HOST_USER, 
     password=settings.EMAIL_HOST_PASSWORD, 
     use_tls=settings.EMAIL_USE_TLS  
       ) as connection:  
           subject = request.POST.get("subject")  
           email_from = settings.EMAIL_HOST_USER  
           recipient_list = [request.POST.get("email"), ]  
           message = request.POST.get("message")  
           EmailMessage(subject, message, email_from, recipient_list, connection=connection).send()  
 
   return render(request, 'home.html')



def withdraw(request):
    if cur_customer is None:
        # Handle the case when cur_customer is None
        # Redirect the user to an appropriate page or display an error message
        return HttpResponse("Error: No customer information found. Please try again.")

    accounts = cur_customer.accounts
    msg="<br>Enter a valid account no. and also check for ur balance!</p><br>"
    if request.method == "POST":
        acc_num=int(request.POST.get('acc_no'))
        amount=int(request.POST.get('amount'))
        print('requestPOST=',acc_num,type(acc_num))
        #print('account dict:',accounts.keys())
        if acc_num in accounts:
            #acc_obj= accounts[acc_num]
            acc_q=Account_Data.objects.get(Account_number=acc_num)
            balance=acc_q.Balance
            print("balance:",balance)
            if(balance>=amount):
                trans=Classes.Account(acc_q)
                trans.create_transaction(amount,"withdraw")
                balance-=amount
                acc_q.Balance=balance
                print("balance:",acc_q.Balance)
                acc_q.save()
                cur_customer.accounts[acc_num].account_details.Balance-=amount
                msg="<td>Withdrawn Successfully!</td><br>"
            else:
                msg="<td>Not sufficient balance!</td><br>"
            
        else:
            msg="<p>Invalid account number</p><br>"
    return render(request, 'InfinityFinance/withdraw.html',{'customer':cur_customer, 'accounts':accounts,'msg':msg})

    #'customer':cur_customer, 'accounts':accounts

def deposit(request):
    accounts = cur_customer.accounts
    msg = ""
    if request.method == "POST":
        acc_num = int(request.POST.get('acc_no'))
        amount = int(request.POST.get('amount'))
        if acc_num in accounts:
            acc_q = Account_Data.objects.get(Account_number=acc_num)
            balance = acc_q.Balance
            trans = Classes.Account(acc_q)
            trans.create_transaction(amount, "deposit")
            balance += amount
            acc_q.Balance = balance
            acc_q.save()
            cur_customer.accounts[acc_num].account_details.Balance += amount
            msg = "<td>Deposited Successfully!</td><br>"
        else:
            msg = "<p>Invalid account number</p><br>"
    return render(request, 'InfinityFinance/deposit.html', {'customer': cur_customer, 'accounts': accounts, 'msg': msg})


def stat_gen(request):
    accounts = cur_customer.accounts
    print(accounts)
    msg=""
    all_transactions = {}
    for acc in accounts:
        print("acc_no:",acc)
        acc_q=Account_Data.objects.get(Account_number=int(acc))
        trans=Classes.Account(acc_q)
        #trans_rec=Transactions.objects.filter(Account_number_id=int(acc))
        #print("trans_rec:",trans_rec)
        transaction=trans.get_transaction_log()
        trans_objs_list = list(transaction.values())
        all_transactions[acc] = all_transactions.get(acc, [])+trans_objs_list
        print("trans:",transaction)
    return render(request, 'InfinityFinance/stat_gen.html',{'customer':cur_customer, 'accounts':accounts, 'transaction':all_transactions,'msg':msg})

def get_transaction_action(request):
    accounts = cur_customer.accounts
    print("got:", request.GET)
    msg="filter"
    button_action = request.GET['account_action']
    all_transactions = {}
    if(button_action == 'withdraw'):
        for acc in accounts:
            transaction=Transactions.objects.filter(Account_number_id=int(acc),Type="withdraw")
            print("withdraw:",transaction)
            all_transactions[acc] = list(transaction)
    elif(button_action == 'deposit'):
        for acc in accounts:
            transaction=Transactions.objects.filter(Account_number_id=int(acc),Type="deposit")
            all_transactions[acc] = list(transaction)
    elif(button_action == 'all'):
        return redirect('InfinityFinance:stat_gen')
    #print("Account created successfully")
    print("all_trans:", all_transactions)
    return render(request,'InfinityFinance/stat_gen.html',{'customer':cur_customer, 'accounts':accounts, 'transaction':all_transactions,'msg':msg});

def get_function_chosen(request):
    print(request.GET) 
    #print("Got menu") 
    menu_chosen = request.GET['function_chosen']
    if(menu_chosen=='view_accounts'):
        return redirect('InfinityFinance:account_management') #name of view given in urls.py
    elif(menu_chosen=='withdraw'):
        return redirect('InfinityFinance:withdraw') #name of view given in urls.py
    elif(menu_chosen=='deposit'):
        return redirect('InfinityFinance:deposit') #name of view given in urls.py
    elif(menu_chosen=='stat_gen'):
        return redirect('InfinityFinance:stat_gen') #name of view given in urls.py
    
def get_account_action(request):
    print("got:", request.GET)
    account_action = request.GET['account_action']
    #err_msg=""
    if(account_action == 'create'):
        cur_customer.create_account()
    elif(account_action == 'close'):
        print(request.GET)
        print("account:", cur_customer.accounts)
        close_Account_number = int(request.GET['close_Account_number'])
        #if(close_Account_number not in accounts):
        #    err_msg = "Invalid Account number!"
        #else:
        cur_customer.close_account(close_Account_number)
    else:
        print("Got neither create nor close")
    #print("Account created successfully")
    return redirect('InfinityFinance:account_management')


    
def pay_bill(request):
    bill_id = request.GET['bill_id']
    print("bill_id", bill_id)
    bill_obj = Bills.objects.get(id=bill_id)
    bill_obj.Completed = True
    bill_obj.save()
    return redirect('InfinityFinance:show_due_bills')
           
'''    
#Testing classes
def test_classes(request):
    print("got to test classes")
    login_obj = Classes.Login_Details('anj', 'anj123')
    cust_obj = Classes.Customer(login_obj)
    acc_obj = Classes.Account(1111)
    new_acc_obj = Classes.New_Account(111, cust_obj)
    new_cust_obj = Classes.New_Customer(login_obj, 'john', 'addr1', '100101')
'''

