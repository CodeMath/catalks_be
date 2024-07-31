import uuid

from django.db import models


class ChatRoomModel(models.Model):
    room_uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=30, verbose_name="채팅방 이름", help_text="커스터 마이징", null=True, blank=True)

    def __str__(self):
        if self.name:
            return f"{self.room_uid} | {self.name}"
        else:
            return f"{self.room_uid}"

