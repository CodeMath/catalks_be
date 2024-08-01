import uuid
from datetime import datetime
from dataclasses import dataclass


@dataclass
class Message:
    message_id: uuid.UUID
    user_id: uuid.UUID
    room_id: uuid.UUID
    content: str
    timestamp: datetime = datetime.now()

    def __post_init__(self):
        if not self.message_id:
            self.message_id = uuid.uuid4()
