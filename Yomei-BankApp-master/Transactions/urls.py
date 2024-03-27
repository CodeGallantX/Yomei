from django.urls import path
from . import views

# Assign urls here
urlpatterns = [
    path('', views.transaction_list, name= 'transaction-list'), # homepage shows all
    path('make-transaction/', views.make_transaction, name="make-transaction"),
]