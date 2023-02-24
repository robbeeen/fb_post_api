import unittest

import pytest
from fb_post.storages.post_storage_implementation import \
    PostStorageImplementation
from fb_post.tests.factories.models import UserFactory, PostFactory, \
    PostDtoFactory


@pytest.mark.django_db
class TestGetPostDetails(unittest.TestCase):

    def test_get_post_details(self):
        # arrange
        UserFactory()
        PostFactory()
        expected_post_dto = PostDtoFactory()
        post_storage = PostStorageImplementation()

        # act
        actual_post_dto = post_storage.get_post_details(post_id=1)

        # arrange
        assert expected_post_dto == actual_post_dto

