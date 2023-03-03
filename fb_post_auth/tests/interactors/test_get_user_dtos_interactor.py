import unittest
from typing import List
from unittest.mock import create_autospec
from fb_post_auth.interactors.get_user_dtos_interactor import \
    GetUserDtosInteractor
from fb_post_auth.interactors.storage_interfaces.user_storage_interface import \
    UserStorageInterface
from fb_post_auth.tests.factories.storage_dtos import UserDtoFactory


class TestGetUserDtosInteractor(unittest.TestCase):
    def test_get_user_dtos(self):
        # Arrange
        user_ids = [1, 2]
        expected = List[UserDtoFactory]
        user_storage = create_autospec(UserStorageInterface)
        interactor = GetUserDtosInteractor(user_storage)
        user_storage.generate_users_dtos.return_value = List[UserDtoFactory]
        # Act
        response = interactor.get_user_dtos(user_ids=user_ids)

        # Assert
        user_storage.generate_users_dtos.assert_called_once_with([1, 2])
        assert expected == response
