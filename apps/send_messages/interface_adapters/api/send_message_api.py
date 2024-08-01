import uuid
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from apps.send_messages.domain.use_cases.messages_use_cases import MessagesUseCases
from apps.send_messages.interface_adapters.gateways.django_messages_repository import DjangoMessagesRepository
from apps.send_messages.serializers import MessageSerializer, SendMessageSerializer


class MessagesAPIViewSet(viewsets.ViewSet):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.use_case = MessagesUseCases(DjangoMessagesRepository())

    @swagger_auto_schema(
        tags=['message'],
        operation_summary='채팅 내역 pagination',
        operation_description='''
        특정 방 채팅 내역 조회 
        limit: 30
        offset: 1
        ''',
        manual_parameters=[
            openapi.Parameter('limit', openapi.IN_QUERY, description="메시지 수 기본값: 30",
                              type=openapi.TYPE_INTEGER),
            openapi.Parameter('offset', openapi.IN_QUERY,
                              description="인덱스(페이지)",
                              type=openapi.TYPE_INTEGER)
        ],
        responses={200: MessageSerializer(many=True)}
    )
    def retrieve(self, request, pk=None):
        limit = request.query_params.get('limit')
        offset = request.query_params.get('offset')

        try:
            room_id = uuid.UUID(pk)
        except ValueError:
            return Response({'detail': 'Invalid UUID format'}, status=status.HTTP_400_BAD_REQUEST)

        message_pagination = self.use_case.repository.get_messages(room_id=room_id, limit=limit, offset=offset)
        serializer = MessageSerializer(message_pagination, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        tags=['message'],
        operation_summary='채팅 전송',
        operation_description='''
        내용 전송
        ''',
        request_body=SendMessageSerializer(),
        responses={201: MessageSerializer()}
    )
    def create(self, request):
        try:
            room_id = uuid.UUID(request.data.get('room_id'))
            content = request.data.get('content')

        except ValueError:
            return Response({'detail': 'Invalid UUID format and none content data'}, status=status.HTTP_400_BAD_REQUEST)

        create_message = self.use_case.send_message(
            room_id=room_id,
            user_id=request.user.user_id,
            content=content
        )
        serializer = MessageSerializer(create_message)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
