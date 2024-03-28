
# In Account.urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('<str:account_number>/', views.account_detail, name='account_detail'), 
    path('login/', Account.signin, name='login'),
    path('logout/', infinity_views.signout, name='logout'),
    path('register/', infinity_views.register, name='register'),
    # Add other URLs as needed
]
