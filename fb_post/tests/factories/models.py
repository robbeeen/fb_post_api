import datetime
import factory
import typing

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
    name = factory.Sequence(lambda n: 'user %s' % n)
    profile_pic = factory.LazyAttribute(lambda o: '%s@url' % o.name)


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    id = factory.Sequence(lambda n: n + 1)
    content = factory.Sequence(lambda n: 'Content %s' % n)
    posted_at = datetime.datetime(2023, 2, 1, 15, 6, 0)
    posted_by_id = factory.sequence(lambda n: n + 1)


class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Comment

    id = factory.sequence(lambda n: n + 1)
    content = factory.sequence(lambda n: " content %s" % n)
    commented_at = datetime.datetime(2023, 2, 1, 15, 6, 0)
    commented_by_id = factory.sequence(lambda n: n + 1)
    post_id = factory.sequence(lambda n: n + 1)
    parent_comment_id = None


class ReactionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Reaction

    post_id = factory.sequence(lambda n: n + 1)
    comment_id = factory.sequence(lambda n: n + 1)
    reaction = None
    reacted_at = datetime.datetime(2023, 2, 1, 15, 6, 0)
    reacted_by_id = factory.sequence(lambda n: n + 1)


class PostDtoFactory(factory.Factory):
    class Meta:
        model = PostDto

    post_id = factory.sequence(lambda n: n + 1)
    content = factory.sequence(lambda n: 'Content %s' % n)
    posted_at = datetime.datetime(2023, 2, 1, 15, 6, 0)
    posted_by_id = factory.sequence(lambda n: n + 1)


class CommentDtoFactory(factory.Factory):
    class Meta:
        model = CommentDto

    comment_id = factory.sequence(lambda n: n + 1)
    comment_content = factory.sequence(lambda n: " content %s" % n)
    commented_at = datetime.datetime(2023, 2, 1, 15, 6, 0)
    commented_by_id = factory.sequence(lambda n: n + 1)
    post_id = factory.sequence(lambda n: n + 1)
    parent_comment_id = None


class UserDtoFactory(factory.Factory):
    class Meta:
        model = UserDto

    user_id = factory.sequence(lambda n: n + 1)
    name = factory.Sequence(lambda n: 'user %s' % n)
    profile_pic = factory.LazyAttribute(lambda o: '%s@url' % o.name)

class ReactionDtoFactory(factory.Factory):
    class Meta:
        model = ReactionDto

    type: str
    post_id: typing.Optional[int] = None
    comment_id: typing.Optional[int] = None

