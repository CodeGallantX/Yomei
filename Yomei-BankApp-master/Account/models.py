from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Personal Information
    full_name = models.CharField(max_length=255)
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    id_number = models.CharField(max_length=50, null=True, blank=True)
    # Financial Information
    account_number = models.CharField(max_length=20, unique=True)
    ACCOUNT_TYPES = [
        ('savings', 'Savings Account'),
        ('current', 'Current Account'),
    ]
    account_type = models.CharField(max_length=10, choices=ACCOUNT_TYPES)
    is_active = models.BooleanField(default=True)
    account_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    # Security Information
    security_questions = models.TextField(null=True, blank=True)
    two_factor_auth_enabled = models.BooleanField(default=False)
    # Preferences
    language_preference = models.CharField(max_length=20, default='en')
    currency_preference = models.CharField(max_length=3, default='USD')
    notification_settings = models.BooleanField(default=True)
    # Additional Details
    subscription_status = models.BooleanField(default=False)
    membership_level = models.CharField(max_length=50, null=True, blank=True)
    plan_details = models.TextField(null=True, blank=True)
    account_creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name


class UserBankAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=20, unique=True)
    ACCOUNT_TYPES = [
        ('savings', 'Savings Account'),
        ('current', 'Current Account'),
    ]
    account_type = models.CharField(max_length=10, choices=ACCOUNT_TYPES)
    is_active = models.BooleanField(default=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    # Add other fields as needed

    def __str__(self):
        return f"{self.user.username}'s Bank Account"

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_number = models.CharField(max_length = 20, unique=True)
    balance = models.DecimalField(max_digits = 10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.user.username}'s Wallet"

