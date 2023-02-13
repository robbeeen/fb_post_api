from abc import ABC
from abc import abstractmethod



class PresenterInterface(ABC):

    @abstractmethod
    def raise_exception_for_invalid_user(self):
        pass

    @abstractmethod
    def post_details_response(self, post_id: int):
        pass