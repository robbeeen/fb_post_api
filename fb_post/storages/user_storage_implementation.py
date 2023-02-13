from fb_post.models.user import User
from fb_post.interactors.storage_interfaces.user_storage_interface import \
    UserStorageInterface


class UserStorageImplementation(UserStorageInterface):

    def is_user_exists(self, user_id: int) -> bool:
        return User.objects.filter(id=user_id).exists()
