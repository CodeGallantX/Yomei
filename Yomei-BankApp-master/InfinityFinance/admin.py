from django.contrib import admin
from .models import Customer
from Transactions.models import Transaction
from Account.models import Account


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('Cust_ID', 'Name', 'Phone_no', 'Email')

class AccountAdmin(admin.ModelAdmin):
    list_display = ('Account_number', 'Owner', 'Balance')

class TransactionsAdmin(admin.ModelAdmin):
    list_display = ('Trans_ID', 'Account_number', 'Amount', 'Type')

'''class MoneyTransfersAdmin(admin.ModelAdmin):
    list_display = ('Trans_ID', 'From_Account_number', 'To_Account_number', 'Amount')
'''

class BillsAdmin(admin.ModelAdmin):
    list_display = ('id', 'Amount', 'Completed')

admin.site.register(Customer)
admin.site.register(Account)
admin.site.register(Transaction)
#admin.site.register(Money_Transfers)
