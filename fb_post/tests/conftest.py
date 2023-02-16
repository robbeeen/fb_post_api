import pytest

from fb_post.tests.factories.models import UserFactory


@pytest.fixture(autouse=True)
def reset_model_factory_sequences():
    UserFactory.reset_sequence()