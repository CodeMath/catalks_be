from app.chat_rooms.domain.repositories.chat_room_repository import ChatRoomRepository
from app.chat_rooms.domain.entities.chat_room import ChatRoom
import uuid


class ChatRoomUseCase:
    def __init__(self, repository: ChatRoomRepository) -> None:
        self.repository = repository

    def create_chat_room(self, name: str) -> ChatRoom:
        """
        Creates a new chat room
        :param name: name of chatroom
        :return: Chatroom object
        """
        chat_room = ChatRoom(room_uid=uuid.uuid4(), name=name)
        self.repository.save(chat_room)
        return chat_room

    def rename_chat_room(self, room_uid: uuid.UUID, new_name: str):
        """
        Renames a chat room
        :param room_uid: uuid.UUID4()
        :param new_name: new name of chatroom
        :return:
        """
        chat_room = self.repository.find_by_id(room_uid)
        chat_room.change_name(new_name)
        self.repository.save(chat_room)


