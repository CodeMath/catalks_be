from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
import uuid
from apps.participations.domain.use_cases.chat_participation_use_cases import ChatParticipationUseCase
from apps.participations.interface_adapters.gateways.django_chat_participation_repository import DjangoChatParticipationRepository
from apps.participations.frameworks_drivers.participations.serializers import ChatParticipationSerializer

class ChatParticipationViewSet(viewsets.ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.use_case = ChatParticipationUseCase(DjangoChatParticipationRepository())

    @swagger_auto_schema(responses={200: ChatParticipationSerializer(many=True)})
    def list(self, request):
        participations = self.use_case.repository.find_all()
        serializer = ChatParticipationSerializer(participations, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=ChatParticipationSerializer, responses={201: ChatParticipationSerializer})
    def create(self, request):
        room_id = request.data.get('room_id')
        user_id = request.data.get('user_id')

        try:
            room_uuid = uuid.UUID(room_id)
            user_uuid = uuid.UUID(user_id)
        except ValueError:
            raise ValidationError("Invalid UUID format")

        participation = self.use_case.join_room(room_uuid, user_uuid)
        serializer = ChatParticipationSerializer(participation)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
