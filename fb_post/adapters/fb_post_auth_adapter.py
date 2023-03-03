from dataclasses import dataclass
from typing import List


@dataclass()
class UserDto:
    name: str
    user_id: int
    profile_pic: str


class FbPostAuthAdapter:
    @property
    def interface(self):
        from fb_post_auth.app_interfaces.service_interface import \
            ServiceInterface
        return ServiceInterface()

    def is_user_exists(self, user_id: int) -> bool:
        return self.interface.get_user(user_id=user_id)

    def get_user_dtos(self, user_ids: List[int]) -> List[UserDto]:
        user_dtos = self.interface.get_user_dto_list(user_ids=user_ids)
        return user_dtos
