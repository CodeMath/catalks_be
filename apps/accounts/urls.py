from django.urls import path
from apps.accounts.interface_adapters.api.accounts_api import UserCreateView

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='register'),
]
