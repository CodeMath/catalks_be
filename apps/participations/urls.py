from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.participations.interface_adapters.api.chat_participation_api import *


router = DefaultRouter()
router.register(r'party', ChatParticipationViewSet, basename='party')

urlpatterns = [
    path('', include(router.urls)),
]