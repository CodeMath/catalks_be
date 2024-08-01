import uuid
from apps.send_messages.domain.repositories.messages_repository import MessagesRepository
from apps.send_messages.domain.entities.messages import Message
from apps.send_messages.models import MessagesModel
from django.core.paginator import Paginator


class DjangoMessagesRepository(MessagesRepository):

    def save(self, message: Message) -> None:
        message_model = MessagesModel(
            message_id=message.message_id,
            room_id=message.room_id,
            user_id=message.user_id,
            content=message.content,
            timestamp=message.timestamp
        )
        message_model.save()

    def get_messages(self, room_id: uuid.UUID, limit: int, offset: int) -> list[Message]:
        get_messages_query = MessagesModel.objects.filter(room_id=room_id).order_by('-timestamp')
        if limit and offset:
            paginator = Paginator(get_messages_query, limit)
            messages_pagination = paginator.get_page(offset)
        else:
            paginator = Paginator(get_messages_query, 30)
            messages_pagination = paginator.get_page(1)

        return messages_pagination
