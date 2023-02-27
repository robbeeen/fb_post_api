from abc import ABC
from abc import abstractmethod

from django.http import HttpResponse

from fb_post.interactors.presenter_interfaces.dtos import GetPostResponseDto


class PresenterInterface(ABC):

    @abstractmethod
    def get_invalid_user_response(self) -> HttpResponse:
        pass

    @abstractmethod
    def get_success_post_response(self, post_id: int) -> HttpResponse:
        pass

    @abstractmethod
    def get_success_get_post_response(
            self, response_dto: GetPostResponseDto) -> HttpResponse:
        pass

    @abstractmethod
    def get_invalid_get_post_response(self) -> HttpResponse:
        pass
