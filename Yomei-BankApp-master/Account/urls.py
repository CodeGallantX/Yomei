from django.urls import path
from . import views

# Assign urls here
urlpatterns = [
    path('<str:account_number>/', views.account_detail, name='account_detail' ),
]