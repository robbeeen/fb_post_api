import unittest

import pytest

from fb_post.interactors.storage_interfaces.dtos import UserDto
from fb_post.storages.post_storage_implementation import \
    PostStorageImplementation
from fb_post.storages.user_storage_implementation import \
    UserStorageImplementation
from fb_post.tests.factories.models import UserFactory, PostFactory
from fb_post.tests.factories.storage_dtos import UserDtoFactory


@pytest.mark.django_db
class TestGetPostUser(unittest.TestCase):
    def test_get_users_dtos(self):
        # Arrange
        UserFactory()
        UserFactory()
        expected_user_dto = [UserDtoFactory(),
                             UserDtoFactory()]
        user_storage = UserStorageImplementation()

        # Act
        actual_user_dto = user_storage.get_users_dtos([1, 2])

        # Assert
        assert expected_user_dto == actual_user_dto
