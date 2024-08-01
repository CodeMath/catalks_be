import uuid

from django.db import models


class MessagesModel(models.Model):
    message_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    room_id = models.UUIDField()
    user_id = models.UUIDField()
    content = models.TextField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"[{self.message_id}] / {self.timestamp}"

