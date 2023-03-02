import unittest

import pytest

from fb_post.storages.comment_storage_implementation import \
    CommentStorageImplementation
from fb_post.tests.factories.models import CommentFactory, \
    PostFactory
from fb_post.tests.factories.storage_dtos import CommentDtoFactory


@pytest.mark.django_db
class TestCommentStorageImplementation(unittest.TestCase):
    def test_get_comments_on_post(self):
        # Arrange
        PostFactory()
        CommentFactory()
        comment_storage = CommentStorageImplementation()
        expected_comment_dtos = [
            CommentDtoFactory()
        ]

        # Act
        actual_comment_dtos = comment_storage.get_comments_on_post(post_id=1)

        # Assert
        assert expected_comment_dtos == actual_comment_dtos

    def test_get_reply_dto(self):
        # Arrange
        PostFactory()
        CommentFactory(post_id=1)
        CommentFactory(post_id=None, parent_comment_id=1)
        CommentFactory(post_id=None, parent_comment_id=1)
        comment_storage = CommentStorageImplementation()
        expected_comment_dtos = [
            CommentDtoFactory(comment_id=2, commented_by_id=2,
                              parent_comment_id=1, post_id=None,comment_content=' content 1'),
            CommentDtoFactory(comment_id=3, commented_by_id=3,
                              parent_comment_id=1, post_id=None,comment_content=' content 2'),

        ]

        # Act
        actual_comment_dtos = comment_storage.get_replies_dtos(
            parent_comment_ids=[1])

        # Assert
        assert expected_comment_dtos == actual_comment_dtos
