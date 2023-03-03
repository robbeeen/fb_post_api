from abc import ABC
from abc import abstractmethod
from typing import List

from django.http import HttpResponse

from fb_post.interactors.presenter_interfaces.dtos import GetPostResponseDto


class PresenterInterfaceGetAllPost(ABC):

    @abstractmethod
    def get_success_all_post_response(self, response_dtos: List[
                GetPostResponseDto]) -> HttpResponse:
        pass