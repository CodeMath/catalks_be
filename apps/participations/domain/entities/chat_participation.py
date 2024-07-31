from dataclasses import dataclass
from datetime import datetime
from typing import Union
import uuid


@dataclass
class ChatParticipation:
    room_id: uuid.UUID
    user_id: uuid.UUID
    joined_at: Union[datetime, None]