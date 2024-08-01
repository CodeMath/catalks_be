import factory
import uuid
from faker import Faker
from apps.send_messages.models import MessagesModel

faker = Faker()


class MessagesFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = MessagesModel

    message_id = factory.LazyFunction(uuid.uuid4)
    room_id = factory.LazyFunction(uuid.uuid4)
    user_id = factory.LazyFunction(uuid.uuid4)
    content = factory.LazyFunction(faker.text)
    timestamp = factory.LazyFunction(faker.date_time_this_year)
