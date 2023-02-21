from abc import ABC, abstractmethod
from typing import List, Tuple

from fb_post.interactors.storage_interfaces.dtos import CommentDto, UserDto
from fb_post.models.comment import Comment


class CommentStorageInterface(ABC):
    @abstractmethod
    def get_comments_on_post(self, post_id) -> List[CommentDto]:
        pass

    @abstractmethod
    def get_reply_dto(self, parent_comment_ids: List[int]) -> List[CommentDto]:
        pass
