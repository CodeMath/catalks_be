from rest_framework import serializers
from apps.chat_rooms.models import ChatRoomModel


class ChatRoomModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatRoomModel
        fields = ["room_uid", "name"]
        