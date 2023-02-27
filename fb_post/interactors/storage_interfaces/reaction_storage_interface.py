from abc import ABC, abstractmethod
from typing import List

from fb_post.interactors.storage_interfaces.dtos import ReactionDto


class ReactionStorageInterface(ABC):
    @abstractmethod
    def get_reactions_on_post(self, post_id: int) -> List[ReactionDto]:
        pass

    @abstractmethod
    def get_reactions_on_comments(self, comment_ids: List[int]) -> List[
        ReactionDto]:
        pass
