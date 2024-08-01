from abc import ABC, abstractmethod
from apps.chat_rooms.domain.entities.chat_room import ChatRoom
import uuid
"""상속을 위한 추상 클래스"""


class ChatRoomRepository(ABC):

    @abstractmethod
    def save(self, chat_room: ChatRoom) -> None:
        """
        방 저장
        :param chat_room: 채팅방 엔티티
        :return:
        """
        pass

    @abstractmethod
    def find_by_id(self, room_uid: uuid.UUID) -> ChatRoom:
        """
        방 찾기
        :param room_uid: 방 UID
        :return:
        """
        pass

    @abstractmethod
    def find_all(self) -> list[ChatRoom]:
        """
        방 전체 조회
        :return:
        """
        pass
