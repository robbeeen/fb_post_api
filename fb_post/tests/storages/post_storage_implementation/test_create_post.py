import pytest

from fb_post.tests.factories.models import UserFactory, PostFactory
import unittest
from fb_post.models.post import Post

from fb_post.storages.post_storage_implementation import \
    PostStorageImplementation


class CreatePostTest(unittest.TestCase):
    @pytest.mark.django_db
    def test_create_post_creates_new_post(self):
        # Arrange
        user_id = 1
        post_content = "New Post"
        expected_output = True
        post_storage = PostStorageImplementation()
        user = UserFactory(id=user_id)

        # Act
        post_id = post_storage.create_post(user_id=user.id,
                                           post_content=post_content)
        # Assert
        actual_output = Post.objects.filter(id=post_id).exists()
        assert actual_output == expected_output
