from abc import ABC, abstractmethod
from apps.send_messages.domain.entities.messages import Message
import uuid


class MessagesRepository(ABC):

    @abstractmethod
    def save(self, message: Message) -> None:
        """
        메시지 저장(보내기)
        :param message: 메시지 엔티티
        :return:
        """
        pass

    @abstractmethod
    def get_messages(self, room_id: uuid.UUID, limit: int, offset: int) -> list[Message]:
        """
        해당 방 전체 메시지 반환
        :param room_id: 방 UID
        :param limit: 메시지 한도
        :param offset: 페이징
        :return:
        """
        pass