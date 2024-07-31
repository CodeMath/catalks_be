from django.db import models
import uuid


class ChatParticipationModel(models.Model):
    room_id = models.UUIDField()
    user_id = models.UUIDField()
    joined_at = models.DateTimeField(auto_now_add=True)
