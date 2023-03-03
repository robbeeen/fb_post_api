import pytest

from fb_post_auth.tests.factories.models import UserFactory
from fb_post_auth.tests.factories.storage_dtos import UserDtoFactory


@pytest.fixture(autouse=True)
def reset_model_factory_sequences():
    UserFactory.reset_sequence()
    UserDtoFactory.reset_sequence()
