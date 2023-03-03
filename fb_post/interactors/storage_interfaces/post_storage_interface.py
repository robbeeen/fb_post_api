from abc import abstractmethod
from abc import ABC
from typing import List

from fb_post.interactors.storage_interfaces.dtos import PostDto
from fb_post.models.post import Post


class PostStorageInterface(ABC):
    @abstractmethod
    def create_post(self, user_id: int, post_content: str) -> int:
        pass

    @abstractmethod
    def is_post_exists(self, post_id: int) -> bool:
        pass

    @abstractmethod
    def get_post_details(self, post_id: int) -> PostDto:
        pass

    @abstractmethod
    def get_all_post_ids(self) -> List[int]:
        pass