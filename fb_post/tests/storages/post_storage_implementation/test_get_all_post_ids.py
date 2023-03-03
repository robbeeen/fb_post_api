import unittest

import pytest

from fb_post.storages.post_storage_implementation import \
    PostStorageImplementation
from fb_post.tests.factories.models import PostFactory
from fb_post.tests.factories.storage_dtos import GetPostParametersDtoFactory


@pytest.mark.django_db
class TestGetAllPostIds(unittest.TestCase):
    def test_get_all_post_ids(self):
        # Arrange
        PostFactory(content="post1")
        PostFactory(content="post2")

        expected_output = [1]
        post_storage = PostStorageImplementation()

        # Act
        actual_output = post_storage.get_all_post_ids(
            GetPostParametersDtoFactory(sortby='id',
                                        filterby='st1', sortby_order='ASC'))

        # Assert
        assert actual_output == expected_output
