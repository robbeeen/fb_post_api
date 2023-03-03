from typing import List

from fb_post_auth.interactors.get_is_user_exists_interactor import \
    GetIsUserExistsInteractor
from fb_post_auth.interactors.get_user_dtos_interactor import \
    GetUserDtosInteractor
from fb_post_auth.interactors.storage_interfaces.dtos import UserDto
from fb_post_auth.storages.user_storage_implementation import \
    UserStorageImplementation


class ServiceInterface:
    @staticmethod
    def get_user(user_id: int) -> bool:
        user_storage = UserStorageImplementation()
        interactor = GetIsUserExistsInteractor(user_storage)
        return interactor.get_is_user_exists(user_id=user_id)

    @staticmethod
    def get_user_dto_list(user_ids: List[int]) -> List[UserDto]:
        user_storage = UserStorageImplementation()
        interactor = GetUserDtosInteractor(user_storage)
        return interactor.get_user_dtos(user_ids=user_ids)
