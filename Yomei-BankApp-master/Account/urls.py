
# In Account.urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('<str:account_number>/', views.account_detail, name='account_detail'),
    # Add other URLs as needed
]
