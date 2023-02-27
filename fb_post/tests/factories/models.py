import datetime
import factory
import typing
from fb_post.constants.enums import ReactionENUM

from fb_post.interactors.storage_interfaces.dtos import PostDto, CommentDto, \
    UserDto, ReactionDto
from fb_post.models.comment import Comment
from fb_post.models.reaction import Reaction
from fb_post.models.user import User
from fb_post.models.post import Post


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    id = factory.sequence(lambda n: n + 1)
    name = factory.Sequence(lambda n: f" user_{n+1}")
    profile_pic = factory.LazyAttribute(lambda o: f" {o.name}@url")


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    id = factory.Sequence(lambda n: n + 1)
    content = factory.Sequence(lambda n: f" content {n}")
    posted_at = datetime.datetime(2023, 2, 1, 15, 6, 0)
    posted_by_id = factory.sequence(lambda n: n + 1)


class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Comment

    id = factory.sequence(lambda n: n + 1)
    content = factory.sequence(lambda n: f" content {n}")
    commented_at = datetime.datetime(2023, 2, 1, 15, 6, 0)
    commented_by_id = factory.sequence(lambda n: n + 1)
    post_id = factory.sequence(lambda n: n + 1)
    parent_comment_id = None


class ReactionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Reaction

    post_id = factory.sequence(lambda n: n + 1)
    comment_id = factory.sequence(lambda n: n + 1)
    reaction = factory.Iterator(["HAHA", "WOW", "SAD"])
    reacted_at = datetime.datetime(2023, 2, 1, 15, 6, 0)
    reacted_by_id = factory.sequence(lambda n: n + 1)
