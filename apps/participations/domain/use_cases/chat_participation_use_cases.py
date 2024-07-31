import uuid
from datetime import datetime
from apps.participations.domain.entities.chat_participation import ChatParticipation
from apps.participations.domain.repositories.chat_participation_repository import ChatParticipationRepository


class ChatParticipationUseCase:
    def __init__(self, repository: ChatParticipationRepository) -> None:
        self.repository = repository

    def join_room(self, room_id: uuid.UUID, user_id: uuid.UUID) -> ChatParticipation:
        try:
            # 이미 존재
            participation = self.repository.find_by_room_and_user(room_id=room_id, user_id=user_id)
        except BaseException:
            print("New Joined becz, not exists")
            participation = ChatParticipation(room_id=room_id, user_id=user_id, joined_at=datetime.now())
            self.repository.save(participation)
        return participation
