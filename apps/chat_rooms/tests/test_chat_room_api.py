import uuid

import pytest
from django.urls import reverse

from apps.chat_rooms.tests.chat_room_factories import ChatRoomFactory
from apps.chat_rooms.models import ChatRoomModel
from apps.accounts.tests.conftest import *

@pytest.mark.django_db
def test_create_chat_room(authenticated_client):
    """
    채팅방 생성 코드
    :param authenticated_client:
    :return:
    """
    url = reverse('chatroom-list')
    data = {'name': 'Test Chat Room'}
    response = authenticated_client.post(url, data, format='json')

    assert response.status_code == 201
    assert ChatRoomModel.objects.count() == 1
    assert ChatRoomModel.objects.get().name == 'Test Chat Room'


@pytest.mark.django_db
def test_list_chat_rooms(authenticated_client):
    """
    채팅방 리스트 조회 코드
    :param authenticated_client:
    :return:
    """
    ChatRoomFactory.create_batch(5)

    url = reverse('chatroom-list')
    response = authenticated_client.get(url, format='json')

    assert response.status_code == 200
    assert len(response.data) == 5


@pytest.mark.django_db
def test_retrieve_chat_room(authenticated_client):
    """
    채팅방 1개 조회 코드
    :param authenticated_client:
    :return:
    """
    chat_room = ChatRoomFactory()

    url = reverse('chatroom-detail', args=[chat_room.room_uid])
    response = authenticated_client.get(url, format='json')

    assert response.status_code == 200
    assert response.data['name'] == chat_room.name


@pytest.mark.django_db
def test_retrieve_none_uuid_chat_room(authenticated_client):
    """
    채팅방 1개 조회 UUID 없는 형태 코드
    :param authenticated_client:
    :return:
    """
    chat_room = "123"

    url = reverse('chatroom-detail', args=[chat_room])
    response = authenticated_client.get(url, format='json')

    assert response.status_code == 400
    assert response.data['detail'] == "Invalid UUID format"


@pytest.mark.django_db
def test_retrieve_not_found_chat_room(authenticated_client):
    """
    채팅방 1개 없는 케이스 코드
    :param authenticated_client:
    :return:
    """
    chat_room = ChatRoomFactory()
    change_room_uid = str(chat_room.room_uid)[:-1] + "9"
    url = reverse('chatroom-detail', args=[change_room_uid])
    response = authenticated_client.get(url, format='json')

    assert response.status_code == 404
    assert response.data['detail'] == "Not found"


@pytest.mark.django_db
def test_update_chat_room(authenticated_client):
    """
    채팅방 이름 변경 코드
    :param authenticated_client:
    :return:
    """
    chat_room = ChatRoomFactory()
    url = reverse('chatroom-detail', args=[chat_room.room_uid])
    data = {'name': 'Updated Chat Room Name'}
    response = authenticated_client.put(url, data, format='json')

    assert response.status_code == 204
    chat_room.refresh_from_db()
    assert chat_room.name == 'Updated Chat Room Name'
