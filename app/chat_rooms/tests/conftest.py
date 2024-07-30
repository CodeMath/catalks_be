import pytest
from rest_framework.test import APIClient
from django.urls import reverse

from app.chat_rooms.tests.user_factories import UserFactory
from app.chat_rooms.frameworks_drivers.chat_rooms.models import ChatRoomModel


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def authenticated_client(api_client):
    user = UserFactory()
    token = UserFactory.get_token(user)
    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
    return api_client
