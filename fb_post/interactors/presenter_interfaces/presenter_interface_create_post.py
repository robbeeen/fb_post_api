from abc import ABC
from abc import abstractmethod

from django.http import HttpResponse

from fb_post.interactors.presenter_interfaces.dtos import GetPostResponseDto


class PresenterInterfaceCreatePost(ABC):

    @abstractmethod
    def get_invalid_user_response(self) -> HttpResponse:
        pass

    @abstractmethod
    def get_success_post_response(self, post_id: int) -> HttpResponse:
        pass

