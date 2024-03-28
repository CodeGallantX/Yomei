from collections import UserDict
from sqlite3 import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from Transactions.models import Transaction
from .models import Account
from .models import UserProfile, UserBankAccount, AccountData

# Create views here

def account_detail(request, account_number):
    # Retrieve account details based on account_number
    # Implement your logic here
    return render(request, 'account_detail.html', {'account': account_details})      


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        username = request.POST['username']  # Add this line to get the username

        try:
            user = User.objects.create_user(username=username, password=pass1, first_name=first_name, last_name=last_name, email=email)
            messages.success(request, 'Your account has been successfully created!')
            return redirect('dashboard')
        except IntegrityError:
            messages.error(request, "Username already exists")
            return redirect('register')

    return render(request, 'InfinityFinance/register.html')



def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')  # Correct field name to 'password'

        # Authenticate user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Login user if authentication successful
            login(request, user)
            return redirect('dashboard')  # Redirect to the dashboard upon successful login
        else:
            # Display error message if authentication failed
            messages.error(request, "Invalid username or password.")
            return redirect('home')  # Redirect to the home page if authentication fails

    # If request method is not POST, render the login page
    return render(request, 'InfinityFinance/login.html')



def signout(request):
    logout(request)  # Call the logout function to log out the user
    messages.success(request, "Logged out successfully!!")
    return redirect('home')
