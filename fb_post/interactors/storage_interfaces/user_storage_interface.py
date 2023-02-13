from abc import abstractmethod
from abc import ABC


class UserStorageInterface(ABC):
    @abstractmethod
    def is_user_exists(self, user_id: int) -> bool:
        pass
