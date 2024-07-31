import pytest
from django.urls import reverse

from apps.accounts.tests.user_factories import UserFactory
from apps.accounts.models import CustomUser


@pytest.mark.django_db
def test_register_user(api_client):
    """
    회원가입 코드
    :param api_client:
    :return:
    """
    url = reverse('register')
    data = {'email': 'asd@asd.com', "password": "<PASSWORD>"}
    response = api_client.post(url, data, format='json')

    assert response.status_code == 201
    assert CustomUser.objects.count() == 1
    assert CustomUser.objects.get().email == 'asd@asd.com'
