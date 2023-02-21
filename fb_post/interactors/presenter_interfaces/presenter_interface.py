from abc import ABC
from abc import abstractmethod

from django.http import HttpResponse

from fb_post.interactors.storage_interfaces.dtos import ResponseDto


class PresenterInterface(ABC):

    @abstractmethod
    def get_invalid_user_response(self) -> HttpResponse:
        pass

    @abstractmethod
    def get_success_post_response(self, post_id: int) -> HttpResponse:
        pass

    @abstractmethod
    def success_get_post_response(self, response_dto: ResponseDto) ->HttpResponse:
        pass

    @abstractmethod
    def failed_get_post_response(self) -> HttpResponse:
        pass
