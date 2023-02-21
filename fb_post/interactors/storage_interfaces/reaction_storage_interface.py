from abc import ABC, abstractmethod
from typing import List


class ReactionStorageInterface(ABC):
    @abstractmethod
    def get_reactions(self, post_id, comment_ids):
        pass
