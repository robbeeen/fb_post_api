from fb_post_auth.exceptions.custom_exceptions import InvalidUserException
from fb_post_auth.interactors.storage_interfaces.user_storage_interface import \
    UserStorageInterface


class GetIsUserExistsInteractor:
    def __init__(self, user_storage: UserStorageInterface):
        self.user_storage = user_storage

    def get_is_user_exists(self, user_id: int) -> bool:
        is_user_exists = self.user_storage.is_user_exists(
            user_id=user_id)

        return is_user_exists



