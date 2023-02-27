import json
import pytest

from fb_post.interactors.presenter_interfaces.dtos import GetPostResponseDto
from fb_post.presenters.presenter_implementation import PresenterImplementation
from fb_post.tests.factories.storage_dtos import PostDtoFactory, \
    CommentDtoFactory, UserDtoFactory, ReactionDtoFactory


@pytest.mark.django_db
class TestPresenterGetPost:

    def test_response_for_invalid_post(self):
        # Arrange
        presenter = PresenterImplementation()

        expected_response = {
            "response": "Post Not Found",
            "http_status_code": 400,
            "res_status": "INVALID_POST_ID"
        }

        # Act
        response = presenter.get_invalid_get_post_response()

        # Assert
        assert json.loads(response.content) == expected_response

    def test_response_for_valid_post(self, snapshot):
        # Arrange

        response_dto = GetPostResponseDto(
            user_dtos=[UserDtoFactory()],
            post_dto=PostDtoFactory(content='Content 1'),
            comment_dtos=[CommentDtoFactory(comment_id=1, post_id=1)],
            reply_dtos=[CommentDtoFactory(comment_id=2, post_id=None,
                                          parent_comment_id=1)],
            reactions_on_post_dtos=[
                ReactionDtoFactory(post_id=1, type="WOW", comment_id=None)],
            reactions_on_comments_dtos=[
                ReactionDtoFactory(post_id=None, type="LIT", comment_id=1),
                ReactionDtoFactory(post_id=None, type="WOW", comment_id=1)
                ]
        )
        presenter = PresenterImplementation()

        # Act
        response = presenter.get_success_get_post_response(response_dto)

        # Assert
        snapshot.assert_match(json.loads(response.content), "response_content")
        snapshot.assert_match(response.status_code, "response_status_code")

    def test_response_for_valid_post_only(self, snapshot):
        # Arrange

        response_dto = GetPostResponseDto(
            user_dtos=[UserDtoFactory()],
            post_dto=PostDtoFactory(content='Content 1'),
            comment_dtos=[],
            reply_dtos=[],
            reactions_on_post_dtos=[],
            reactions_on_comments_dtos=[]
        )
        presenter = PresenterImplementation()

        # Act
        response = presenter.get_success_get_post_response(response_dto)

        # Assert
        snapshot.assert_match(json.loads(response.content), "response_content")
        snapshot.assert_match(response.status_code, "response_status_code")

    def test_response_for_valid_post_and_comment_only(self, snapshot):
        # Arrange
        response_dto = GetPostResponseDto(
            user_dtos=[UserDtoFactory()],
            post_dto=PostDtoFactory(content='Content 1'),
            comment_dtos=[CommentDtoFactory(comment_id=1, post_id=1)],
            reply_dtos=[],
            reactions_on_post_dtos=[],
            reactions_on_comments_dtos=[]
        )
        presenter = PresenterImplementation()

        # Act
        response = presenter.get_success_get_post_response(response_dto)

        # Assert
        snapshot.assert_match(json.loads(response.content), "response_content")
        snapshot.assert_match(response.status_code, "response_status_code")

    def test_response_for_valid_post_comment_replies_only(self, snapshot):
        # Arrange

        response_dto = GetPostResponseDto(
            user_dtos=[UserDtoFactory()],
            post_dto=PostDtoFactory(content='Content 1'),
            comment_dtos=[CommentDtoFactory(comment_id=1, post_id=1)],
            reply_dtos=[CommentDtoFactory(comment_id=2, post_id=None,
                                          parent_comment_id=1)],
            reactions_on_post_dtos=[],
            reactions_on_comments_dtos=[]
        )
        presenter = PresenterImplementation()

        # Act
        response = presenter.get_success_get_post_response(response_dto)

        # Assert
        snapshot.assert_match(json.loads(response.content), "response_content")
        snapshot.assert_match(response.status_code, "response_status_code")

    def test_response_for_valid_post_comment_reactions_only(self, snapshot):
        # Arrange
        response_dto = GetPostResponseDto(
            user_dtos=[UserDtoFactory()],
            post_dto=PostDtoFactory(content='Content 1'),
            comment_dtos=[CommentDtoFactory(comment_id=1, post_id=1)],
            reply_dtos=[],

            reactions_on_post_dtos=[
                ReactionDtoFactory(post_id=1, type="WOW", comment_id=None)],
            reactions_on_comments_dtos=[
                ReactionDtoFactory(post_id=None, type="LIT", comment_id=1)]

        )
        presenter = PresenterImplementation()

        # Act
        response = presenter.get_success_get_post_response(response_dto)

        # Assert
        snapshot.assert_match(json.loads(response.content), "response_content")
        snapshot.assert_match(response.status_code, "response_status_code")

    def test_response_for_valid_post_reactions_only(self, snapshot):
        # Arrange

        response_dto = GetPostResponseDto(
            user_dtos=[UserDtoFactory()],
            post_dto=PostDtoFactory(content='Content 1'),
            comment_dtos=[],
            reply_dtos=[],
            reactions_on_post_dtos=[
                ReactionDtoFactory(post_id=1, type="WOW", comment_id=None)],
            reactions_on_comments_dtos=[])

        presenter = PresenterImplementation()

        # Act
        response = presenter.get_success_get_post_response(response_dto)

        # Assert
        snapshot.assert_match(json.loads(response.content), "response_content")
        snapshot.assert_match(response.status_code, "response_status_code")

    def test_response_for_valid_comment_reactions_only(self, snapshot):
        # Arrange
        response_dto = GetPostResponseDto(
            user_dtos=[UserDtoFactory()],
            post_dto=PostDtoFactory(content='Content 1'),
            comment_dtos=[CommentDtoFactory(comment_id=1, post_id=1)],
            reply_dtos=[],
            reactions_on_post_dtos=[],
            reactions_on_comments_dtos=[
                ReactionDtoFactory(post_id=None, type="LIT", comment_id=1)])

        presenter = PresenterImplementation()

        # Act
        response = presenter.get_success_get_post_response(response_dto)

        # Assert
        snapshot.assert_match(json.loads(response.content), "response_content")
        snapshot.assert_match(response.status_code, "response_status_code")
