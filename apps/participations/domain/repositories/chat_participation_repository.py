from abc import ABC, abstractmethod
from typing import List
import uuid
from apps.participations.domain.entities.chat_participation import ChatParticipation


class ChatParticipationRepository(ABC):
    @abstractmethod
    def save(self, chat_participation: ChatParticipation) -> None:
        """
        채팅방 입장
        :param chat_participation: 채팅방 입장 엔티티
        :return:
        """
        pass

    @abstractmethod
    def find_user_by_room(self, room_id: uuid.UUID) -> list[ChatParticipation]:
        """
        특정 방 사용자 조회
        :param room_id: 방 UID
        :return:
        """
        pass

    @abstractmethod
    def find_room_by_user(self, user_id: uuid.UUID) -> List[ChatParticipation]:
        """
        특정 사용자 입장한 방 조회
        :param user_id: 사용자 UID
        :return:
        """
        pass
