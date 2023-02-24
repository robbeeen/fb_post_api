import unittest

import pytest

from fb_post.interactors.storage_interfaces.dtos import UserDto
from fb_post.storages.post_storage_implementation import \
    PostStorageImplementation
from fb_post.storages.user_storage_implementation import \
    UserStorageImplementation
from fb_post.tests.factories.models import UserFactory, PostFactory


@pytest.mark.django_db
class TestGetPostUserDetails(unittest.TestCase):
    def test_get_user_details(self):
        # Arrange
        UserFactory()
        expected_user_dto = [UserDto(
            user_id=1,
            name="user 0",
            profile_pic="user 0@url"
        )]
        post = PostFactory()
        user_storage = UserStorageImplementation()
        post_storage = PostStorageImplementation()
        # Act
        actual_user_dto = user_storage.get_user_details([1])
        post_exists = post_storage.is_post_exists(post_id=post.pk)
        # Assert
        assert post_exists == True
        assert expected_user_dto == actual_user_dto
