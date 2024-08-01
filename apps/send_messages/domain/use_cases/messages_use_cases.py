from apps.send_messages.domain.entities.messages import Message
from apps.send_messages.domain.repositories.messages_repository import MessagesRepository
from datetime import datetime
import uuid


class MessagesUseCases:
    def __init__(self, repository: MessagesRepository):
        self.repository = repository

    def send_message(self, content: str, room_id: uuid.UUID, user_id: uuid.UUID) -> Message:
        new_message = Message(
            message_id=uuid.uuid4(),
            room_id=room_id,
            user_id=user_id,
            content=content,
            timestamp=datetime.now()
        )
        self.repository.save(new_message)
        return new_message

