import json

import pytest
from unittest.mock import create_autospec, Mock

import snapshottest

from fb_post.interactors.get_post_interactor import GetPostInteractor
from fb_post.interactors.presenter_interfaces.presenter_interface import \
    PresenterInterface
from fb_post.interactors.storage_interfaces.comment_storage_interface import \
    CommentStorageInterface
from fb_post.interactors.storage_interfaces.dtos import \
    ResponseDto
from fb_post.interactors.storage_interfaces.post_storage_interface import \
    PostStorageInterface
from fb_post.interactors.storage_interfaces.reaction_storage_interface import \
    ReactionStorageInterface
from fb_post.interactors.storage_interfaces.user_storage_interface import \
    UserStorageInterface
from fb_post.tests.factories.models import PostDtoFactory, ReactionDtoFactory, \
    UserDtoFactory, CommentDtoFactory


class TestInteractorGetPost:

    @pytest.fixture()
    def response_dto(self):
        response_dto = ResponseDto(
            user_dtos=[UserDtoFactory()],
            post_dto=PostDtoFactory(content='Content 1'),
            comment_dtos=[CommentDtoFactory(comment_id=1, post_id=1)],
            reply_dtos=[CommentDtoFactory(comment_id=2, post_id=None,
                                          parent_comment_id=1)],
            reactions_dtos=[ ReactionDtoFactory(post_id=None, type="LIT", comment_id=1),
                ReactionDtoFactory(post_id=None, type="WOW", comment_id=1),
                ReactionDtoFactory(post_id=1, type="WOW", comment_id=None)
               ]
        )

        return response_dto

    def test_get_post_with_valid_post_id(self, response_dto,snapshot):
        post_id = 1
        reaction_on_post_dto = [ReactionDtoFactory(
            post_id=1,
            comment_id=None,
            type="WOW"
        )]
        reaction_on_comment_dtos = [
            ReactionDtoFactory(post_id=None, type="LIT", comment_id=1),
            ReactionDtoFactory(post_id=None, type="WOW", comment_id=1)]

        post_storage = create_autospec(PostStorageInterface)
        user_storage = create_autospec(UserStorageInterface)
        comment_storage = create_autospec(CommentStorageInterface)
        reaction_storage = create_autospec(ReactionStorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = GetPostInteractor(
            post_storage=post_storage,
            user_storage=user_storage,
            comment_storage=comment_storage,
            reaction_storage=reaction_storage,
            presenter=presenter,
            post_id=post_id
        )
        post_storage.is_post_exists.return_value = True
        post_storage.get_post_details.return_value = response_dto.post_dto
        comment_storage.get_comments_on_post.return_value = response_dto.comment_dtos
        comment_storage.get_reply_dto.return_value = response_dto.reply_dtos
        user_storage.get_user_details.return_value = response_dto.user_dtos
        reaction_storage.get_reactions_on_post.return_value = reaction_on_post_dto
        reaction_storage.get_reactions_on_comments.return_value = reaction_on_comment_dtos

        comments_ids = list(comment_dto.comment_id for comment_dto in
                            response_dto.comment_dtos)
        comments_ids.extend(
            reply_dto.comment_id for reply_dto in response_dto.reply_dtos)
        commenters_ids = list(comment_dto.commented_by_id for comment_dto in
                              response_dto.comment_dtos)
        commenters_ids.append(response_dto.post_dto.posted_by_id)
        commenters_ids.extend(
            reply_dto.commented_by_id for reply_dto in response_dto.reply_dtos)
        # Act
        interactor.get_post_wrapper(post_id)

        # Assert
        post_storage.is_post_exists.assert_called_once_with(
            post_id=post_id)
        post_storage.get_post_details.assert_called_once()
        comment_storage.get_comments_on_post.assert_called_once()
        comment_storage.get_reply_dto.assert_called_once()
        user_storage.get_user_details.assert_called_once()
        reaction_storage.get_reactions_on_post.assert_called_once()
        reaction_storage.get_reactions_on_comments.assert_called_once()
        presenter.success_get_post_response.assert_called_once_with(response_dto)

    def test_get_post_with_invalid_post(self):
        # Arrange
        post_id = 0
        post_storage = create_autospec(PostStorageInterface)
        user_storage = create_autospec(UserStorageInterface)
        comment_storage = create_autospec(CommentStorageInterface)
        reaction_storage = create_autospec(ReactionStorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = GetPostInteractor(
            post_storage=post_storage,
            user_storage=user_storage,
            comment_storage=comment_storage,
            reaction_storage=reaction_storage,
            presenter=presenter,
            post_id=post_id
        )
        post_storage.is_post_exists.return_value = False
        presenter_response = Mock()
        presenter.failed_get_post_response.return_value = presenter_response

        # Act
        response = interactor.get_post_wrapper(post_id=post_id)

        # Assert
        post_storage.is_post_exists.assert_called_once_with(post_id=post_id)
        presenter.failed_get_post_response.assert_called_once()

        assert response == presenter_response
