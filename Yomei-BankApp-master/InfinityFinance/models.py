from django.db import models
from django.contrib.auth.models import User

'''
class Bill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    is_paid = models.BooleanField(default=False)

class AirtimePurchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    phone_number = models.CharField(max_length=15)
    is_successful = models.BooleanField(default=False)
    

'''

# Create your models here.
class Customer(models.Model):
    Cust_ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=200)
    Phone_no = models.CharField(max_length=10)
    #Fixed length can't be specified. Only max_length can be.
    Email = models.EmailField()
    #Username = models.CharField(max_length=30)
    #Password = models.CharField(max_length=30)
    class Meta:
        db_table = 'customer'

'''    
class Deposits(models.Model): 
    Trans_ID = models.AutoField(primary_key=True)
    Account_number = models.ForeignKey(Account, on_delete=models.CASCADE)
    Amount = models.FloatField()
    class Meta:
        db_table = 'deposits'
        
class Withdraws(models.Model): 
    Trans_ID = models.AutoField(primary_key=True)
    Account_number = models.ForeignKey(Account, on_delete=models.CASCADE)
    Amount = models.FloatField()
    class Meta:
        db_table = 'withdraws' 
'''