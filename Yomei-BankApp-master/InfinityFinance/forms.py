from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class DepositForm(forms.Form):
    amount = forms.DecimalField(max_digits=10, decimal_places=2)
    account_type = forms.ChoiceField(label="Choose Account:", choices=["Savings Account", "Current Account", "Business Account"], required=True)

class WithdrawForm(forms.Form):
    amount = forms.DecimalField(max_digits=10, decimal_places=2)

'''class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')
    phone_number = forms.CharField(max_length=15, help_text='Required. Enter your phone number.')
    first_name = forms.CharField(max_length=30, help_text='Required. Enter your first name.')
    last_name = forms.CharField(max_length=30, help_text='Required. Enter your last name.')
    password1 = forms.CharField(widget=forms.PasswordInput, help_text='Required. Enter a password.')
    password2 = forms.CharField(widget=forms.PasswordInput, help_text='Required. Enter the same password again.')

    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'first_name', 'last_name', 'password1', 'password2']

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        # Add custom validation logic here, such as checking for a specific format or length
        if not phone_number.isdigit():
            raise forms.ValidationError('Phone number must contain only digits.')
        return phone_number'''

