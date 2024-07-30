from django.db import models
import uuid


class ChatRoomModel(models.Model):
    room_uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=30, null=True, blank=True)


class User(models.Model):
    user_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    username = models.CharField(max_length=30)


class ChatParticipationModel(models.Model):
    room_id = models.UUIDField()
    user_id = models.UUIDField()
    joined_at = models.DateTimeField(auto_now_add=True)
