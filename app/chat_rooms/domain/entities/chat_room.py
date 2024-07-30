import uuid
from dataclasses import dataclass
"""
@dataclass 를 통해서, 해당 클레스를 `데이터 클레스`화
* 데이터 클레스는 __init__ , __repr__, __eq__ 메서드 자동 생성
* 데이터의 불변성 추가하려면, @dataclass(frozen=True)
* 필드 값에 따라 대소 비교 추가하려면, @dataclass(order=True)
* 데이터 클레스의 인스턴스는 기본적으로 hashable 하지 않음 => set의 값이나 dict의 키로 사용 불가
따라서 hashable하게 하려면, unsafe_hash 옵션 추가

"""


@dataclass(order=True)
class ChatRoom:
    room_uid: uuid.UUID
    name: str = None

    def __post_init__(self):
        if not self.room_uid:
            self.room_uid = uuid.uuid4()

    def change_name(self, new_name: str):
        if not new_name:
            raise ValueError("채팅방 이름을 입력해주세요.")
        self.name = new_name
