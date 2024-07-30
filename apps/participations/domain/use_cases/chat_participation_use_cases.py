from apps.participations.domain.entities.chat_participation import ChatParticipation
from apps.participations.domain.repositories.chat_participation_repository import ChatParticipationRepository
import uuid


class ChatParticipationUseCase:
    def __init__(self, repository: ChatParticipationRepository) -> None:
        self.repository = repository

    def join_room(self, room_id: uuid.UUID, user_id: uuid.UUID) -> ChatParticipation:
        participation = ChatParticipation(room_id=room_id, user_id=user_id)
        self.repository.save(participation)
        return participation
