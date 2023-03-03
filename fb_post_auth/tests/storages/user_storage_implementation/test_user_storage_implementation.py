import unittest

import pytest

from fb_post_auth.storages.user_storage_implementation import \
    UserStorageImplementation
from fb_post_auth.tests.factories.models import UserFactory
from fb_post_auth.tests.factories.storage_dtos import UserDtoFactory


@pytest.mark.django_db
class TestUserStorageImplementation(unittest.TestCase):
    def test_check_is_user_exists(self):
        # Arrange
        UserFactory()
        user_id = 1
        expected_output = True
        user_storage = UserStorageImplementation()

        # Act
        actual_output = user_storage.is_user_exists(
            user_id=user_id
        )
        # Assert

        assert expected_output == actual_output

    def test_check_is_invalid_user(self):
        # Arrange
        user_id = 0
        expected_output = False
        user_storage = UserStorageImplementation()
        # Act
        actual_output = user_storage.is_user_exists(
            user_id=user_id
        )
        # Assert

        assert expected_output == actual_output

    def test_get_users_dtos(self):
        # Arrange
        UserFactory(id=1)
        UserFactory(id=2)
        expected_user_dto = [UserDtoFactory(user_id=1),
                             UserDtoFactory(user_id=2)]
        user_storage = UserStorageImplementation()

        # Act
        actual_user_dto = user_storage.generate_users_dtos([1, 2])

        # Assert
        assert expected_user_dto == actual_user_dto
