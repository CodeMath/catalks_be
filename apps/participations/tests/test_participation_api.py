import uuid

import pytest
from django.urls import reverse

from apps.chat_rooms.tests.chat_room_factories import ChatRoomFactory
from apps.chat_rooms.models import ChatRoomModel
from apps.participations.tests.participation_facotries import ChatParticipationFactory
from apps.participations.models import ChatParticipationModel

from apps.accounts.tests.conftest import *


@pytest.mark.django_db
def test_participation_joined_chatroom(authenticated_client):
    """
    채팅방 생성 후 조인
    :param authenticated_client:
    :return:
    """
    chat_room = ChatRoomFactory()
    assert ChatRoomModel.objects.count() == 1

    url = reverse('party-list')
    data = {"room_id": chat_room.room_uid}
    response = authenticated_client.post(url, data, format='json')

    assert response.status_code == 201


@pytest.mark.django_db
def test_participation_api(authenticated_client):
    """
    채팅방 참여 방 수
    :param authenticated_client:
    :return:
    """
    chat_room = ChatRoomFactory.create_batch(5)
    assert ChatRoomModel.objects.count() == 5
    url = reverse('party-list')

    for room in chat_room[:3]:
        authenticated_client.post(url, {"room_id": room.room_uid}, format='json')

    response = authenticated_client.get(url, format='json')

    assert response.status_code == 200
    assert ChatParticipationModel.objects.count() == 3


@pytest.mark.django_db
def test_account_list_by_retrieve_chat_room(authenticated_client):
    """
    채팅방 접속자 조회
    :param authenticated_client:
    :return:
    """
    chat_room = ChatRoomFactory()
    assert ChatRoomModel.objects.count() == 1

    url = reverse('party-detail', args=[chat_room.room_uid])
    response = authenticated_client.get(url, format='json')

    assert response.status_code == 200