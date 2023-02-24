

from django.http import HttpResponse

from fb_post.exceptions.custom_exceptions import InvalidPostException
from fb_post.interactors.presenter_interfaces.presenter_interface import \
    PresenterInterface
from fb_post.interactors.storage_interfaces.comment_storage_interface import \
    CommentStorageInterface
from fb_post.interactors.storage_interfaces.dtos import ResponseDto
from fb_post.interactors.storage_interfaces.post_storage_interface import \
    PostStorageInterface
from fb_post.interactors.storage_interfaces.reaction_storage_interface import \
    ReactionStorageInterface
from fb_post.interactors.storage_interfaces.user_storage_interface import \
    UserStorageInterface


class GetPostInteractor:
    def __init__(self, user_storage: UserStorageInterface,
                 post_storage: PostStorageInterface,
                 comment_storage: CommentStorageInterface,
                 reaction_storage: ReactionStorageInterface,
                 presenter: PresenterInterface,
                 post_id: int):
        self.user_storage = user_storage
        self.post_storage = post_storage
        self.comment_storage = comment_storage
        self.reaction_storage = reaction_storage
        self.presenter = presenter
        self.post_id = post_id

    def get_post_wrapper(self, post_id: int) -> HttpResponse:
        try:
            response_dto = self.get_post(post_id)
            return self.presenter.success_get_post_response(response_dto)
        except InvalidPostException:
            return self.presenter.failed_get_post_response()

    def get_post(self, post_id) -> ResponseDto:
        self._validate_post_id(post_id)
        post_dto = self.post_storage.get_post_details(post_id=post_id)
        comments_on_post_dtos = self.comment_storage.get_comments_on_post(
            post_dto.post_id)

        comment_ids = []
        for comments_on_post_dto in comments_on_post_dtos:
            comment_ids.append(comments_on_post_dto.comment_id)

        commenter_ids_list = []
        for comments_on_post_dto in comments_on_post_dtos:
            commenter_ids_list.append(comments_on_post_dto.commented_by_id)

        user_ids = commenter_ids_list
        user_ids.append(post_dto.posted_by_id)

        replies_dtos = self.comment_storage.get_reply_dto(comment_ids)

        for replies_dto in replies_dtos:
            comment_ids.append(replies_dto.comment_id)
            user_ids.append(
                replies_dto.commented_by_id)

        user_dtos = self.user_storage.get_user_details(
            user_ids=user_ids)

        reaction_on_post_dto = self.reaction_storage.get_reactions_on_post(
            post_id=post_id)
        reactions_dtos = self.reaction_storage.get_reactions_on_comments(
            comment_ids=comment_ids)
        reactions_dtos.extend(reaction_on_post_dto)
        response_dto = ResponseDto(
            post_dto=post_dto,
            user_dtos=user_dtos,
            comment_dtos=comments_on_post_dtos,
            reply_dtos=replies_dtos,
            reactions_dtos=reactions_dtos
        )

        return response_dto

    def _validate_post_id(self, post_id: int) -> None:
        is_post_not_exists = not self.post_storage.is_post_exists(post_id)
        if is_post_not_exists:
            raise InvalidPostException
