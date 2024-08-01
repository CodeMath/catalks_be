from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.send_messages.interface_adapters.api.send_message_api import *


router = DefaultRouter()
router.register(r'message', MessagesAPIViewSet, basename='message')

urlpatterns = [
    path('', include(router.urls)),
]