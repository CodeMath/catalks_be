import factory
import uuid
from faker import Faker
from apps.participations.models import ChatParticipationModel

faker = Faker()


class ChatParticipationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ChatParticipationModel

    room_id = factory.LazyFunction(uuid.uuid4)
    user_id = factory.LazyFunction(uuid.uuid4)
