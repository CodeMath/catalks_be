from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.exceptions import ValidationError
import uuid

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from app.chat_rooms.domain.use_cases.chat_room_use_cases import ChatRoomUseCase
from app.chat_rooms.frameworks_drivers.chat_rooms.models import ChatRoomModel
from app.chat_rooms.interface_adapter.gateways.orm_chat_room_repository import ORMChatRoomRepository
from app.chat_rooms.frameworks_drivers.chat_rooms.serializers import ChatRoomModelSerializer


class ChatRoomViewSet(viewsets.ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.use_case = ChatRoomUseCase(ORMChatRoomRepository())

    @swagger_auto_schema(request_body=ChatRoomModelSerializer, responses={201: ChatRoomModelSerializer})
    def create(self, request):
        name = request.data.get("name")
        chat_room = self.use_case.create_chat_room(name)
        serializer = ChatRoomModelSerializer(chat_room)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        tags=['chatrooms'],
        operation_summary='''채팅방 리스트''',
        operation_description=
        f'''
        채팅방 리스트 조회
        ''',
        responses={200: ChatRoomModelSerializer(many=True)}
    )
    def list(self, request):
        chat_rooms = self.use_case.repository.find_all()
        serializer = ChatRoomModelSerializer(chat_rooms, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        tags=['chatrooms'],
        operation_summary='''채팅방 1개 조회''',
        operation_description=
        f'''
        UUID로 조회
        ''',
        responses={200: ChatRoomModelSerializer}
    )
    def retrieve(self, request, pk=None):
        try:
            chat_room_uuid = uuid.UUID(pk)
            chat_room = self.use_case.repository.find_by_id(chat_room_uuid)
        except ValueError:
            return Response({"detail": "Invalid UUID format"}, status=status.HTTP_400_BAD_REQUEST)
        except ChatRoomModel.DoesNotExist:
            return Response({"detail": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ChatRoomModelSerializer(chat_room)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'name': openapi.Schema(type=openapi.TYPE_STRING, description='Name of the chat room')
            }
        ),
        responses={204: 'No Content'}
    )
    def update(self, request, pk=None):
        new_name = request.data.get("name")
        self.use_case.rename_chat_room(uuid.UUID(pk), new_name)
        return Response(status=status.HTTP_204_NO_CONTENT)