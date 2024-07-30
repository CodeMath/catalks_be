from rest_framework import generics
from apps.accounts.models import CustomUser
from apps.accounts.serializers import UserSerializer
from rest_framework.permissions import AllowAny

class UserCreateView(generics.CreateAPIView):
    permission_classes = (AllowAny,)

    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
