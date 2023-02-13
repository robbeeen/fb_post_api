from abc import abstractmethod
from abc import ABC

class PostStorageInterface(ABC):
    @abstractmethod
    def create_post(self, user_id: int, post_content: str):
        pass
