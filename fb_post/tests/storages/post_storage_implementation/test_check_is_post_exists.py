import unittest
from unittest.mock import create_autospec

import pytest

from fb_post.storages.post_storage_implementation import \
    PostStorageImplementation
from fb_post.tests.factories.models import PostFactory


class PostExistsOrNotTest(unittest.TestCase):
    @pytest.mark.django_db
    def test_check_is_post_exists(self):
        # Arrange
        expected_output = True
        post_storage = PostStorageImplementation()
        PostFactory()

        # Act
        actual_output = post_storage.is_post_exists(
            post_id=1
        )

        # Assert
        assert expected_output == actual_output

    @pytest.mark.django_db
    def test_check_is_invalid_post(self):
        # Arrange
        expected_output = False
        post_storage = PostStorageImplementation()

        # Act
        actual_output = post_storage.is_post_exists(
            post_id=1
        )
        # Assert

        assert expected_output == actual_output
