from django.forms import forms
from .models import Transaction

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['account',
                  'amount',
                  'trans_type',
                  'description'
                  ]
        
