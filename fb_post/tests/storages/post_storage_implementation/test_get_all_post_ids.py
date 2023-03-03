import unittest

import pytest

from fb_post.storages.post_storage_implementation import \
    PostStorageImplementation
from fb_post.tests.factories.models import PostFactory


@pytest.mark.django_db
class TestGetAllPostIds(unittest.TestCase):
    def test_get_all_post_ids(self):
        # Arrange
        PostFactory()
        PostFactory()
        expected_output = [1, 2]
        post_storage = PostStorageImplementation()

        # Act
        actual_output = post_storage.get_all_post_ids()

        # Assert
        assert actual_output == expected_output
