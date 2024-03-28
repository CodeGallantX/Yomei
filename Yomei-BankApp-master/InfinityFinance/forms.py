from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class DepositForm(forms.Form):
    amount = forms.DecimalField(max_digits=10, decimal_places=2)
    account_type = forms.ChoiceField(label="Choose Account:", choices=["Savings Account", "Current Account", "Business Account"], required=True)

class WithdrawForm(forms.Form):
    amount = forms.DecimalField(max_digits=10, decimal_places=2)


