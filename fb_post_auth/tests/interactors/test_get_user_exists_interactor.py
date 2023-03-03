import unittest
from unittest.mock import create_autospec, Mock

import pytest

from fb_post_auth.interactors.get_is_user_exists_interactor import \
    GetIsUserExistsInteractor
from fb_post_auth.interactors.storage_interfaces.user_storage_interface import \
    UserStorageInterface
from fb_post_auth.tests.factories.models import UserFactory


class TestGetIsUserExistsInteractor(unittest.TestCase):
    def test_for_valid_user(self):
        # Arrange
        user_id = 1
        user_storage = create_autospec(UserStorageInterface)
        user_storage.is_user_exists.return_value = True
        interactor = GetIsUserExistsInteractor(user_storage)
        expected = True
        # Act
        response = interactor.get_is_user_exists(user_id=user_id)

        # Assert
        user_storage.is_user_exists.assert_called_once_with(user_id)
        assert expected == response

    def test_for_invalid_user(self):
        # Arrange
        user_id = 1
        user_storage = create_autospec(UserStorageInterface)
        user_storage.is_user_exists.return_value = False
        interactor = GetIsUserExistsInteractor(user_storage)
        expected = False
        # Act
        response = interactor.get_is_user_exists(user_id=user_id)

        # Assert
        user_storage.is_user_exists.assert_called_once_with(user_id)
        assert expected == response