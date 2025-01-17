import factory
import uuid
from faker import Faker
from apps.chat_rooms.models import ChatRoomModel

faker = Faker()


class ChatRoomFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ChatRoomModel

    room_uid = factory.LazyFunction(uuid.uuid4)
    name = factory.LazyFunction(faker.name)
