import pytest
from unittest.mock import create_autospec, Mock

from fb_post.exceptions.custom_exceptions import InvalidUserException
from fb_post.interactors.create_post_interactor import CreatePostInteractor
from fb_post.interactors.storage_interfaces.post_storage_interface import \
    PostStorageInterface
from fb_post.interactors.storage_interfaces.user_storage_interface import \
    UserStorageInterface
from fb_post.interactors.presenter_interfaces.presenter_interface_create_post import \
    PresenterInterface
from fb_post.tests.factories.models import PostFactory


class TestInteractorCreatePost:

    @pytest.mark.django_db
    def test_create_post_with_user_valid_user(self):
        # Arrange
        user_id = 1
        post_id = 2
        post_content = "New Post"
        post_storage = create_autospec(PostStorageInterface)
        user_storage = create_autospec(UserStorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = CreatePostInteractor(user_storage=user_storage,
                                          post_storage=post_storage,
                                          presenter=presenter,
                                          post_content=post_content)
        user_storage.is_user_exists.return_value = True
        post_storage.create_post.return_value = post_id
        presenter_response = {
            "post_id": post_id
        }
        presenter.get_success_post_response.return_value = presenter_response
        # Act
        response = interactor.create_post_wrapper(user_id=user_id,
                                                  post_content=post_content)
        # Assert
        user_storage.is_user_exists.assert_called_once_with(
            user_id=user_id)
        post_storage.create_post.assert_called_once_with(
            user_id=user_id,
            post_content=post_content)
        presenter.get_success_post_response.assert_called_once_with(post_id)
        assert presenter_response == response

    def test_create_post_with_invalid_user(self):
        # Arrange
        user_id = 0
        post_content = "Invalid Post Content"

        post_storage = create_autospec(PostStorageInterface)
        user_storage = create_autospec(UserStorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = CreatePostInteractor(user_storage=user_storage,
                                          post_storage=post_storage,
                                          presenter=presenter,
                                          post_content=post_content)

        user_storage.is_user_exists.return_value = False
        presenter_response = Mock()
        presenter.get_invalid_user_response.return_value = presenter_response

        # Act
        response = interactor.create_post_wrapper(user_id=user_id,
                                                  post_content=post_content)

        # Assert
        user_storage.is_user_exists.assert_called_once_with(
            user_id=user_id)
        presenter.get_invalid_user_response.assert_called_once()

        assert response == presenter_response
