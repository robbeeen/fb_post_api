import pytest

from fb_post.tests.factories.models import UserFactory, PostFactory, \
    ReactionFactory, CommentFactory, PostDtoFactory, CommentDtoFactory, \
    ReactionDtoFactory, UserDtoFactory


@pytest.fixture(autouse=True)
def reset_model_factory_sequences():
    UserFactory.reset_sequence()
    PostFactory.reset_sequence()
    ReactionFactory.reset_sequence()
    CommentFactory.reset_sequence()
    PostDtoFactory.reset_sequence()
    CommentDtoFactory.reset_sequence()
    ReactionDtoFactory.reset_sequence()
    UserDtoFactory.reset_sequence()
