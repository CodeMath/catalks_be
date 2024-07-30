from abc import ABC, abstractmethod
from apps.chat_rooms.domain.entities.chat_room import ChatRoom
import uuid
"""상속을 위한 추상 클래스"""


class ChatRoomRepository(ABC):

    @abstractmethod
    def save(self, chat_room: ChatRoom) -> None:
        pass

    @abstractmethod
    def find_by_id(self, room_uid: uuid.UUID) -> ChatRoom:
        pass

    @abstractmethod
    def find_all(self) -> list[ChatRoom]:
        pass
