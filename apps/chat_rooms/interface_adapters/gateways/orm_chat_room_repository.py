from apps.chat_rooms.domain.repositories.chat_room_repository import ChatRoomRepository
from apps.chat_rooms.domain.entities.chat_room import ChatRoom
from apps.chat_rooms.models import ChatRoomModel
import uuid


class ORMChatRoomRepository(ChatRoomRepository):
    def save(self, chat_room: ChatRoom) -> None:
        chat_room_model, created = ChatRoomModel.objects.get_or_create(room_uid=chat_room.room_uid)
        chat_room_model.name = chat_room.name
        chat_room_model.save()

    def find_by_id(self, room_uid: uuid.UUID) -> ChatRoom:
        chat_room_model = ChatRoomModel.objects.get(room_uid=room_uid)
        return ChatRoom(room_uid=chat_room_model.room_uid, name=chat_room_model.name)

    def find_all(self) -> list[ChatRoom]:
        chat_room_models = ChatRoomModel.objects.all()
        return [ChatRoom(room_uid=crm.room_uid, name=crm.name) for crm in chat_room_models]
