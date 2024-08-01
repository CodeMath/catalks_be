import pytest
import uuid
from django.urls import reverse

from apps.chat_rooms.tests.chat_room_factories import ChatRoomFactory
from apps.participations.tests.participation_facotries import ChatParticipationFactory
from apps.send_messages.tests.messages_factories import MessagesFactory
from apps.participations.models import ChatParticipationModel

from apps.accounts.tests.conftest import *


@pytest.fixture
def authenticated_client_join_chatroom(authenticated_client):
    chat_room = ChatRoomFactory()
    url = reverse('party-list')
    data = {"room_id": chat_room.room_uid}
    authenticated_client.post(url, data, format='json')

    return authenticated_client


@pytest.mark.django_db
def test_send_messages(authenticated_client_join_chatroom):
    url = reverse('party-list')

    response = authenticated_client_join_chatroom.get(url, format='json')
    assert response.status_code == 200
    assert ChatParticipationModel.objects.count() == 1

    room_id = response.data[0]["room_id"]
    send_url = reverse('message-list')
    data = {"room_id": room_id, 'content': 'Hello World!'}
    response = authenticated_client_join_chatroom.post(send_url, data, format='json')
    assert response.status_code == 201
    assert response.data["room_id"] == room_id


@pytest.mark.django_db
def test_get_list_messages(authenticated_client_join_chatroom):
    url = reverse('party-list')

    response = authenticated_client_join_chatroom.get(url, format='json')
    assert response.status_code == 200
    assert ChatParticipationModel.objects.count() == 1
    room_id = response.data[0]["room_id"]

    send_url = reverse('message-list')
    contents = MessagesFactory.create_batch(5)
    for msg in contents:
        data = {"room_id": room_id, 'content': msg.content}
        authenticated_client_join_chatroom.post(send_url, data, format='json')

    list_url = reverse('message-detail', args=[room_id])

    response = authenticated_client_join_chatroom.get(f"{list_url}?limit=30&offset=1", format='json')

    assert response.status_code == 200
    assert len(response.data) == 5
