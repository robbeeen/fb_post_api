from unittest.mock import Mock, create_autospec

import pytest

from fb_post.interactors.presenter_interfaces.presenter_interface import \
    PresenterInterface
from fb_post.interactors.storage_interfaces.user_storage_interface import \
    UserStorageInterface


class TestPresenterCreatePost:
    def test_response_for_valid_user(self):
        post_id = 2
        presenter = create_autospec(PresenterInterface)
        presenter_response = Mock()
        presenter.get_success_post_response.return_value = presenter_response

        # Act
        response = presenter.get_success_post_response(post_id)

        # Assert
        assert response == presenter_response

    def test_response_for_invalid_user(self):
        # Arrange
        user_storage = create_autospec(UserStorageInterface)
        presenter = create_autospec(PresenterInterface)

        user_storage.is_user_exists.return_value = False
        presenter_response = Mock()
        presenter.get_invalid_user_response.return_value = presenter_response

        # Act
        response = presenter.get_invalid_user_response()

        # Assert
        presenter.get_invalid_user_response.assert_called_once()
        assert response == presenter_response
