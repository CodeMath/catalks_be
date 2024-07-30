from participations.domain.entities.chat_participation import ChatParticipation
from participations.domain.repositories.chat_participation_repository import ChatParticipationRepository
from participations.frameworks_drivers.participations.models import ChatParticipationModel
import uuid


class DjangoChatParticipationRepository(ChatParticipationRepository):
    def save(self, chat_participation: ChatParticipation) -> None:
        participation_model = ChatParticipationModel(
            room_id=chat_participation.room_id,
            user_id=chat_participation.user_id,
            joined_at=chat_participation.joined_at
        )
        participation_model.save()

    def find_by_room_and_user(self, room_id: uuid.UUID, user_id: uuid.UUID) -> ChatParticipation:
        participation_model = ChatParticipationModel.objects.get(room_id=room_id, user_id=user_id)
        return ChatParticipation(
            room_id=participation_model.room_id,
            user_id=participation_model.user_id,
            joined_at=participation_model.joined_at
        )

    def find_all(self) -> List[ChatParticipation]:
        participation_models = ChatParticipationModel.objects.all()
        return [
            ChatParticipation(
                room_id=pm.room_id,
                user_id=pm.user_id,
                joined_at=pm.joined_at
            ) for pm in participation_models
        ]
