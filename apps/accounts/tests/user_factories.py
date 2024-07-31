import factory
import uuid
from faker import Faker
from apps.accounts.models import CustomUser
from rest_framework_simplejwt.tokens import RefreshToken

faker = Faker()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CustomUser

    # username = factory.LazyFunction(faker.user_name)
    email = factory.LazyFunction(faker.email)
    password = factory.PostGenerationMethodCall('set_password', 'password')

    @staticmethod
    def get_token(user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)