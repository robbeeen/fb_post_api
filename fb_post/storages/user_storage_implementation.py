from typing import List

from fb_post.interactors.storage_interfaces.dtos import UserDto
from fb_post.models.user import User
from fb_post.interactors.storage_interfaces.user_storage_interface import \
    UserStorageInterface


class UserStorageImplementation(UserStorageInterface):

    def is_user_exists(self, user_id: int) -> bool:
        return User.objects.filter(id=user_id).exists()

    def get_user_details(self, user_id: int,
                         commenter_details_list: List[int]) -> List[UserDto]:
        users = User.objects.filter(id=user_id,
                                    ) | User.objects.filter(
            id__in=commenter_details_list, )
        user_dtos = [
            self._prepare_commenter_dto(user)
            for user in users
        ]
        return user_dtos

    @staticmethod
    def _prepare_commenter_dto(user):
        return UserDto(
            user_id=user.id,
            name=user.name,
            profile_pic=user.profile_pic
        )
