from rest_framework import serializers
from app.chat_rooms.frameworks_drivers.chat_rooms.models import ChatRoomModel


class ChatRoomModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatRoomModel
        fields = ["room_uid", "name"]
        