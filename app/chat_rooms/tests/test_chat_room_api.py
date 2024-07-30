import pytest
from django.urls import reverse

from app.chat_rooms.tests.factories import ChatRoomFactory
from app.chat_rooms.frameworks_drivers.chat_rooms.models import ChatRoomModel


@pytest.mark.django_db
def test_create_chat_room(authenticated_client):
    url = reverse('chatroom-list')
    data = {'name': 'Test Chat Room'}
    response = authenticated_client.post(url, data, format='json')

    assert response.status_code == 201
    assert ChatRoomModel.objects.count() == 1
    assert ChatRoomModel.objects.get().name == 'Test Chat Room'


@pytest.mark.django_db
def test_list_chat_rooms(authenticated_client):
    ChatRoomFactory.create_batch(5)

    url = reverse('chatroom-list')
    response = authenticated_client.get(url, format='json')

    assert response.status_code == 200
    assert len(response.data) == 5


@pytest.mark.django_db
def test_retrieve_chat_room(authenticated_client):
    chat_room = ChatRoomFactory()

    url = reverse('chatroom-detail', args=[chat_room.room_uid])
    response = authenticated_client.get(url, format='json')

    assert response.status_code == 200
    assert response.data['name'] == chat_room.name


@pytest.mark.django_db
def test_update_chat_room(authenticated_client):
    chat_room = ChatRoomFactory()
    url = reverse('chatroom-detail', args=[chat_room.room_uid])
    data = {'name': 'Updated Chat Room Name'}
    response = authenticated_client.put(url, data, format='json')

    assert response.status_code == 204
    chat_room.refresh_from_db()
    assert chat_room.name == 'Updated Chat Room Name'