import json
import pytest

from fb_post.interactors.presenter_interfaces.dtos import GetPostResponseDto
from fb_post.presenters.get_all_post_presenter_implementation import \
    PresenterImplementationGetAllPost
from fb_post.tests.factories.adapter_dtos import UserDtoFactory
from fb_post.tests.factories.storage_dtos import PostDtoFactory, \
    CommentDtoFactory, ReactionDtoFactory


class TestPresenterGetPost:

    def test_response_for_valid_posts(self, snapshot):
        # Arrange

        response_dto = [GetPostResponseDto(
            user_dtos=[UserDtoFactory(), UserDtoFactory()],
            post_dto=PostDtoFactory(content='Content 1'),
            comment_dtos=[CommentDtoFactory(comment_id=1, post_id=1)],
            reply_dtos=[CommentDtoFactory(comment_id=2, post_id=None,
                                          parent_comment_id=1)],
            reactions_on_post_dtos=[
                ReactionDtoFactory(post_id=1, type="WOW", comment_id=None)],
            reactions_on_comments_dtos=[
                ReactionDtoFactory(post_id=None, type="WOW", comment_id=1),
                ReactionDtoFactory(post_id=None, type="LIT", comment_id=1)
            ]
        ),
            GetPostResponseDto(
                user_dtos=[UserDtoFactory(user_id=2),
                           UserDtoFactory(user_id=3),
                           UserDtoFactory(user_id=4)],
                post_dto=PostDtoFactory(content='Content 1'),
                comment_dtos=[CommentDtoFactory(post_id=2)],
                reply_dtos=[CommentDtoFactory(post_id=None,
                                              parent_comment_id=3)],
                reactions_on_post_dtos=[
                    ReactionDtoFactory(post_id=2, type="WOW",
                                       comment_id=None)],
                reactions_on_comments_dtos=[
                    ReactionDtoFactory(post_id=None, type="WOW", comment_id=3),
                    ReactionDtoFactory(post_id=None, type="LIT", comment_id=3)
                ]
            )
        ]
        presenter = PresenterImplementationGetAllPost()

        # Act
        response = presenter.get_success_all_post_response(response_dto)

        # Assert
        snapshot.assert_match(json.loads(response.content), "response_content")
        snapshot.assert_match(response.status_code, "response_status_code")
