import uuid
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from apps.participations.domain.use_cases.chat_participation_use_cases import ChatParticipationUseCase
from apps.participations.interface_adapters.gateways.django_chat_participation_repository import DjangoChatParticipationRepository
from apps.participations.serializers import CreateChatParticipationSerializer, ChatParticipationSerializer


class ChatParticipationViewSet(viewsets.ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.use_case = ChatParticipationUseCase(DjangoChatParticipationRepository())

    @swagger_auto_schema(
        tags=['party'],
        operation_summary='''들어간 채팅방 리스트''',
        operation_description=
        f'''
        UUID로 조회
        ''',
        responses={200: ChatParticipationSerializer(many=True)})
    def list(self, request):
        participations = self.use_case.repository.find_room_by_user(request.user.user_id)
        serializer = ChatParticipationSerializer(participations, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        tags=['party'],
        operation_summary='''채팅방 들어가기''',
        operation_description=
        f'''
            UUID로 조회
            ''',
        request_body=CreateChatParticipationSerializer, responses={201: ChatParticipationSerializer})
    def create(self, request):
        room_id = request.data.get('room_id')

        try:
            room_uuid = uuid.UUID(room_id)
            user_uuid = request.user.user_id
        except ValueError:
            return Response({"detail": "Invalid UUID format"}, status=status.HTTP_400_BAD_REQUEST)

        participation = self.use_case.join_room(room_uuid, user_uuid)
        serializer = ChatParticipationSerializer(participation)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


    @swagger_auto_schema(
        tags=['party'],
        operation_summary='''채팅방 접속자(join한 사용자 UID 반환)''',
        operation_description=
        f'''
        방 UUID로 조회
        ''',
        responses={200: ChatParticipationSerializer(many=True)})
    def retrieve(self, request, pk=None):
        try:
            room_uuid = uuid.UUID(pk)
        except ValueError:
            return Response({"detail": "Invalid UUID format"}, status=status.HTTP_400_BAD_REQUEST)

        participation = self.use_case.repository.find_user_by_room(
            room_uuid
        )
        serializer = ChatParticipationSerializer(participation, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

