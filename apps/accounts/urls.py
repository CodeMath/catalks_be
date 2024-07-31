from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

from apps.accounts.interface_adapters.api.accounts_api import UserCreateView


urlpatterns = [
    path('register/', UserCreateView.as_view(), name='register'),
    path('signin/', TokenObtainPairView.as_view(), name='signin'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
