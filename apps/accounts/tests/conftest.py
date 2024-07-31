import pytest
from rest_framework.test import APIClient
from django.urls import reverse

from apps.accounts.tests.user_factories import UserFactory


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def authenticated_client(api_client):
    user = UserFactory()
    token = UserFactory.get_token(user)
    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
    return api_client
