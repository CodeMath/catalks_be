from dataclasses import dataclass
from datetime import datetime
import uuid


@dataclass
class ChatParticipation:
    room_uid: uuid.UUID
    user_id: uuid.UUID
    joined_at: datetime
