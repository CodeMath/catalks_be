from rest_framework import serializers
from apps.participations.domain.entities.chat_participation import ChatParticipation


class CreateChatParticipationSerializer(serializers.Serializer):
    room_id = serializers.UUIDField()


class ChatParticipationSerializer(serializers.Serializer):
    room_id = serializers.UUIDField()
    user_id = serializers.UUIDField()
    joined_at = serializers.DateTimeField()
