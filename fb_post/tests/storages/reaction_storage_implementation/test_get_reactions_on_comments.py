import unittest
from fb_post.constants.enums import ReactionENUM
import pytest

from fb_post.interactors.storage_interfaces.dtos import ReactionDto
from fb_post.storages.reaction_storage_implementation import \
    ReactionStorageImplementation
from fb_post.tests.factories.models import PostFactory, ReactionFactory, CommentFactory


@pytest.mark.django_db
class TestGetPostReactionsOnComments(unittest.TestCase):
    @pytest.mark.django_db
    def test_get_reactions_on_comments(self):
        # Arrange
        reaction_storage = ReactionStorageImplementation()
        PostFactory(id=1, posted_by_id=1)
        CommentFactory(id=1, post_id=1, commented_by_id=1)
        ReactionFactory(reaction="WOW",
                        post_id=None,
                        comment_id=1)
        ReactionFactory(reaction="WOW",
                        post_id=None,
                        comment_id=1,
                        )

        expected_reaction_on_comment_dto = [ReactionDto(
            type="WOW",
            comment_id=1
        ),
            ReactionDto(
                type="WOW",
                comment_id=1
            )
        ]

        # Act
        actual_reaction_on_comment_dto = reaction_storage.get_reactions_on_comments(
            [1])

        # Assert
        assert expected_reaction_on_comment_dto == actual_reaction_on_comment_dto
