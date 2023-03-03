import pytest

from fb_post.tests.factories.adapter_dtos import UserDtoFactory
from fb_post.tests.factories.models import PostFactory, \
    ReactionFactory, CommentFactory
from fb_post.tests.factories.storage_dtos import PostDtoFactory, CommentDtoFactory, \
    ReactionDtoFactory


@pytest.fixture(autouse=True)
def reset_model_factory_sequences():
    PostFactory.reset_sequence()
    ReactionFactory.reset_sequence()
    CommentFactory.reset_sequence()
    PostDtoFactory.reset_sequence()
    CommentDtoFactory.reset_sequence()
    ReactionDtoFactory.reset_sequence()
    UserDtoFactory.reset_sequence()
