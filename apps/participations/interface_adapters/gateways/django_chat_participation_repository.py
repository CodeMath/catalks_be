from apps.participations.domain.entities.chat_participation import ChatParticipation
from apps.participations.domain.repositories.chat_participation_repository import ChatParticipationRepository
from apps.participations.models import ChatParticipationModel
import uuid


class DjangoChatParticipationRepository(ChatParticipationRepository):
    def save(self, chat_participation: ChatParticipation) -> None:
        participation_model = ChatParticipationModel(
            room_id=chat_participation.room_id,
            user_id=chat_participation.user_id,
            joined_at=chat_participation.joined_at
        )
        participation_model.save()

    def find_user_by_room(self, room_id: uuid.UUID) -> list[ChatParticipation]:
        participation_model = ChatParticipationModel.objects.filter(room_id=room_id)
        return [
            ChatParticipation(
                room_id=pm.room_id,
                user_id=pm.user_id,
                joined_at=pm.joined_at
            ) for pm in participation_model
        ]

    def find_room_by_user(self, user_id: uuid.UUID) -> list[ChatParticipation]:
        participation_models = ChatParticipationModel.objects.filter(user_id=user_id)
        return [
            ChatParticipation(
                room_id=pm.room_id,
                user_id=pm.user_id,
                joined_at=pm.joined_at
            ) for pm in participation_models
        ]
