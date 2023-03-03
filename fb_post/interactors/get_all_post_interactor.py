from typing import List, Any

from django.http import HttpResponse

from fb_post.adapters.service_adapter import get_service_adapter
from fb_post.interactors.get_post_interactor import GetPostInteractor
from fb_post.interactors.presenter_interfaces.dtos import GetPostResponseDto
from fb_post.interactors.presenter_interfaces.presenter_interface_get_all_post import \
    PresenterInterfaceGetAllPost
from fb_post.interactors.presenter_interfaces.presenter_interface_get_post import \
    PresenterInterfaceGetPost
from fb_post.interactors.storage_interfaces.comment_storage_interface import \
    CommentStorageInterface
from fb_post.interactors.storage_interfaces.dtos import GetPostParametersDto
from fb_post.interactors.storage_interfaces.post_storage_interface import \
    PostStorageInterface
from fb_post.interactors.storage_interfaces.reaction_storage_interface import \
    ReactionStorageInterface


class GetAllPostInteractor:
    def __init__(self, post_storage: PostStorageInterface,
                 comment_storage: CommentStorageInterface,
                 reaction_storage: ReactionStorageInterface,
                 presenter: PresenterInterfaceGetAllPost,
                 get_post_presenter: PresenterInterfaceGetPost):
        self.post_storage = post_storage
        self.comment_storage = comment_storage
        self.reaction_storage = reaction_storage
        self.presenter = presenter
        self.get_post_presenter = get_post_presenter

    def get_all_post_wrapper(self, sortby: str, offset: int,
                             limit: int, filterby: str) -> HttpResponse:
        list_of_response_dtos = self.get_all_post(sortby=sortby,
                                                  offset=offset,
                                                  limit=limit,
                                                  filterby=filterby)
        return self.presenter.get_success_all_post_response(
            list_of_response_dtos)

    def get_all_post(self, sortby: str, offset: int,
                     limit: int, filterby: str) -> \
            List[GetPostResponseDto]:
        post_ids = self.post_storage.get_all_post_ids()
        get_post_interactor = GetPostInteractor(
            post_storage=self.post_storage,
            comment_storage=self.comment_storage,
            reaction_storage=self.reaction_storage,
            presenter=self.get_post_presenter)

        if offset < 0:
            self.presenter.raise_exception_for_invalid_offset_length()
            return

        if limit < 0:
            self.presenter.raise_exception_for_invalid_limit_length()
            return
        get_post_parameters_dto = GetPostParametersDto(
            limit=limit,
            offset=offset,
            sortby=sortby,
            filterby=filterby
        )

        list_of_response_dtos = list(
            get_post_interactor.get_post(post_id=post_id,
                                         get_post_parameters_dto=get_post_parameters_dto)
            for post_id
            in post_ids)
        return list_of_response_dtos
