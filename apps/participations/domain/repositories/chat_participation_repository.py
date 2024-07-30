from abc import ABC, abstractmethod
from typing import List
import uuid
from apps.participations.domain.entities.chat_participation import ChatParticipation


class ChatParticipationRepository(ABC):
    @abstractmethod
    def save(self, chat_participation: ChatParticipation) -> None:
        pass

    @abstractmethod
    def find_by_room_and_user(self, room_id: uuid.UUID, user_id: uuid.UUID) -> ChatParticipation:
        pass

    @abstractmethod
    def find_all(self) -> List[ChatParticipation]:
        pass
