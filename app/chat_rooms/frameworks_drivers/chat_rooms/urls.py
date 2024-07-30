from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.chat_rooms.interface_adapter.api.chat_room_api import ChatRoomViewSet

router = DefaultRouter()
router.register(r'chatrooms', ChatRoomViewSet, basename='chatroom')

urlpatterns = [
    path('', include(router.urls)),
]