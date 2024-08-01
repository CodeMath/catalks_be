from rest_framework import serializers
from apps.send_messages.models import MessagesModel


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessagesModel
        fields = '__all__'


class SendMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessagesModel
        fields = ['room_id', 'content']