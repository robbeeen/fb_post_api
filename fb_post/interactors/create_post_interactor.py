from fb_post.interactors.storage_interfaces.post_storage_interface import \
    PostStorageInterface
from fb_post.interactors.storage_interfaces.user_storage_interface import \
    UserStorageInterface
from fb_post.interactors.presenter_interfaces.presenter_interface_create_post import \
    PresenterInterface
from typing import Any
from fb_post.exceptions.custom_exceptions import InvalidUserException


class CreatePostInteractor:
    def __init__(self, user_storage: UserStorageInterface,
                 post_storage: PostStorageInterface,
                 presenter: PresenterInterface,
                 post_content: str):
        self.user_storage = user_storage
        self.post_storage = post_storage
        self.presenter = presenter
        self.post_content = post_content

    def create_post_wrapper(self, user_id: int, post_content: str) -> Any:
        try:
            post_id = self.create_post(user_id, post_content)
            return self.presenter.get_success_post_response(post_id)
        except InvalidUserException:
            return self.presenter.get_invalid_user_response()

    def create_post(self, user_id: int, post_content: str) -> int:

        self._validate_user_id(user_id)

        post_id = self.post_storage.create_post(user_id=user_id,
                                                post_content=post_content)

        return post_id

    def _validate_user_id(self, user_id: int) -> None:
        is_user_not_exists = not self.user_storage.is_user_exists(
            user_id=user_id)
        if is_user_not_exists:
            raise InvalidUserException
