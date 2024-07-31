from abc import ABC, abstractmethod
from typing import List
import uuid
from apps.participations.domain.entities.chat_participation import ChatParticipation


class ChatParticipationRepository(ABC):
    @abstractmethod
    def save(self, chat_participation: ChatParticipation) -> None:
        pass

    @abstractmethod
    def find_user_by_room(self, room_id: uuid.UUID) -> list[ChatParticipation]:
        pass

    @abstractmethod
    def find_room_by_user(self, user_id: uuid.UUID) -> List[ChatParticipation]:
        pass
