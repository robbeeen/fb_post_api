from unittest.mock import create_autospec

import pytest


from fb_post.storages.user_storage_implementation import \
    UserStorageImplementation
from fb_post.tests.factories.models import UserFactory


@pytest.mark.django_db
def test_check_is_user_exists():
    # Arrange
    user_id = 1
    expected_output = True
    user_storage = UserStorageImplementation()
    user = UserFactory(id=user_id)
    # Act
    actual_output = user_storage.is_user_exists(
        user_id=user.id
    )
    # Assert

    assert expected_output == actual_output


@pytest.mark.django_db
def test_check_is_invalid_user():
    # Arrange
    user_id = 0
    expected_output = False
    user_storage = UserStorageImplementation()

    # Act
    actual_output = user_storage.is_user_exists(
        user_id=user_id
    )
    # Assert

    assert expected_output == actual_output
