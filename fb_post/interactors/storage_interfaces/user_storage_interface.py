from abc import abstractmethod
from abc import ABC
from typing import List

from fb_post.interactors.storage_interfaces.dtos import UserDto


class UserStorageInterface(ABC):
    @abstractmethod
    def is_user_exists(self, user_id: int) -> bool:
        pass

    @abstractmethod
    def get_users_dtos(self, user_ids: List[int]) -> List[UserDto]:
        pass
