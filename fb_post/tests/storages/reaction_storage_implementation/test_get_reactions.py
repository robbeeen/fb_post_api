import unittest

import pytest

from fb_post.interactors.storage_interfaces.dtos import ReactionDto
from fb_post.storages.reaction_storage_implementation import \
    ReactionStorageImplementation
from fb_post.tests.factories.models import PostFactory, ReactionFactory, \
    UserFactory, CommentFactory


@pytest.mark.django_db
class TestGetPostReactionsOnPost(unittest.TestCase):
    @pytest.mark.django_db
    def test_get_reactions_on_post(self):
        # Arrange
        UserFactory(id=1)
        PostFactory(id=1, posted_by_id=1)
        reaction_storage = ReactionStorageImplementation()
        ReactionFactory(reaction="WOW",
                        post_id=1,
                        comment_id=None)
        expected_reaction_on_post_dto = [ReactionDto(
            type="WOW",
            post_id=1,
            comment_id=None
        )]

        # Act
        actual_reaction_on_post_dto = reaction_storage.get_reactions_on_post(
            post_id=1)

        # Assert

        assert expected_reaction_on_post_dto == actual_reaction_on_post_dto
