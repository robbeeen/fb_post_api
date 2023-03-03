from unittest.mock import patch, create_autospec

import pytest

from fb_post.interactors.get_all_post_interactor import GetAllPostInteractor
from fb_post.interactors.get_post_interactor import GetPostInteractor
from fb_post.interactors.presenter_interfaces.dtos import GetPostResponseDto
from fb_post.interactors.presenter_interfaces.presenter_interface_get_all_post import \
    PresenterInterfaceGetAllPost
from fb_post.interactors.presenter_interfaces.presenter_interface_get_post import \
    PresenterInterfaceGetPost
from fb_post.interactors.storage_interfaces.comment_storage_interface import \
    CommentStorageInterface
from fb_post.interactors.storage_interfaces.post_storage_interface import \
    PostStorageInterface
from fb_post.interactors.storage_interfaces.reaction_storage_interface import \
    ReactionStorageInterface
from fb_post.tests.factories.adapter_dtos import UserDtoFactory
from fb_post.tests.factories.models import PostFactory
from fb_post.tests.factories.storage_dtos import PostDtoFactory, \
    CommentDtoFactory, ReactionDtoFactory


class TestGetAllPostInteractor:
    @pytest.fixture()
    @patch('fb_post.adapters.fb_post_auth_adapter.FbPostAuthAdapter.'
           'get_user_dtos')
    def response_dto(self, user_dtos):
        response_dto = GetPostResponseDto(
            post_dto=PostDtoFactory(content='Content 1'),
            user_dtos=user_dtos[1, 2],
            comment_dtos=[CommentDtoFactory(comment_id=1, post_id=1)],
            reply_dtos=[CommentDtoFactory(comment_id=2, post_id=None,
                                          parent_comment_id=1)],
            reactions_on_post_dtos=[
                ReactionDtoFactory(post_id=1, type="WOW", comment_id=None)
            ],
            reactions_on_comments_dtos=[
                ReactionDtoFactory(post_id=None, type="LIT", comment_id=1),
                ReactionDtoFactory(post_id=None, type="WOW", comment_id=1)]
        )

        return response_dto

    @patch('fb_post.interactors.get_post_interactor.'
           'GetPostInteractor.get_post')
    def test_get_all_post_interactor(self, get_post, response_dto):
        # Arrange
        post_ids = [1, 2]
        post_storage = create_autospec(PostStorageInterface)
        comment_storage = create_autospec(CommentStorageInterface)
        reaction_storage = create_autospec(ReactionStorageInterface)
        presenter = create_autospec(PresenterInterfaceGetAllPost)
        get_post_presenter = create_autospec(PresenterInterfaceGetPost)
        interactor = GetAllPostInteractor(post_storage=post_storage,
                                          comment_storage=comment_storage,
                                          reaction_storage=reaction_storage,
                                          presenter=presenter,
                                          get_post_presenter=get_post_presenter)

        post_storage.get_all_post_ids.return_value = post_ids
        list_of_response_dtos = [
            GetPostResponseDto(
                user_dtos=[UserDtoFactory(), UserDtoFactory()],
                post_dto=PostDtoFactory(post_id=1, content='Content 1'),
                comment_dtos=[CommentDtoFactory(comment_id=1, post_id=1)],
                reply_dtos=[CommentDtoFactory(comment_id=2, post_id=None,
                                              parent_comment_id=1)],
                reactions_on_post_dtos=[
                    ReactionDtoFactory(post_id=1, type="WOW",
                                       comment_id=None)],
                reactions_on_comments_dtos=[
                    ReactionDtoFactory(post_id=None, type="WOW", comment_id=1),
                    ReactionDtoFactory(post_id=None, type="LIT", comment_id=1)
                ]
            ),
            GetPostResponseDto(
                user_dtos=[UserDtoFactory(user_id=2),
                           UserDtoFactory(user_id=3),
                           UserDtoFactory(user_id=4)],
                post_dto=PostDtoFactory(post_id=2, content='Content 1'),
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
        get_post.side_effect = list_of_response_dtos

        # Act
        interactor.get_all_post_wrapper(offset=0, limit=10, filterby="",
                                        sortby="", sortby_order="")

        # Assert
        post_storage.get_all_post_ids.assert_called_once()
        presenter.get_success_all_post_response.assert_called_once_with(
            list_of_response_dtos)
