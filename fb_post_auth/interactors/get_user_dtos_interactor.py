from typing import List

from fb_post_auth.interactors.storage_interfaces.dtos import UserDto
from fb_post_auth.interactors.storage_interfaces.user_storage_interface import \
    UserStorageInterface


class GetUserDtosInteractor:
    def __init__(self, user_storage: UserStorageInterface):
        self.user_storage = user_storage

    def get_user_dtos(self, user_ids: List[int]) -> List[UserDto]:
        user_dtos = self.user_storage.generate_users_dtos(
            user_ids=user_ids)
        return user_dtos
