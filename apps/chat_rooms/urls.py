from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.chat_rooms.interface_adapters.api.chat_room_api import ChatRoomViewSet

router = DefaultRouter()
router.register(r'chatrooms', ChatRoomViewSet, basename='chatroom')

urlpatterns = [
    path('', include(router.urls)),
]