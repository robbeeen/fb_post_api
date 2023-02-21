import unittest
from unittest.mock import create_autospec

import pytest

from fb_post.storages.post_storage_implementation import \
    PostStorageImplementation
from fb_post.tests.factories.models import PostFactory


class PostTest(unittest.TestCase):
    @pytest.mark.django_db
    def test_check_is_post_exists(self):
        # Arrange
        post_id = 1
        expected_output = True
        post_storage = PostStorageImplementation
        post = PostFactory(id=post_id)

        # Act
        actual_output = post_storage.is_post_exists(
            post_id=post_id
        )

        # Assert
        assert expected_output == actual_output

    @pytest.mark.django_db
    def test_check_is_invalid_post(self):
        # Arrange
        post_id = 0
        expected_output = False
        user_storage = PostStorageImplementation()

        # Act
        actual_output = user_storage.is_post_exists(
            post_id=post_id
        )
        # Assert

        assert expected_output == actual_output
