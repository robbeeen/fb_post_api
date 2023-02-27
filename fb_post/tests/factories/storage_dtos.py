import datetime
import factory
import typing

from fb_post.constants.enums import ReactionENUM
from fb_post.interactors.storage_interfaces.dtos import CommentDto, PostDto, \
    UserDto, ReactionDto


class PostDtoFactory(factory.Factory):
    class Meta:
        model = PostDto

    post_id = factory.sequence(lambda n: n + 1)
    content = factory.sequence(lambda n: f" content {n}")
    posted_at = datetime.datetime(2023, 2, 1, 15, 6, 0)
    posted_by_id = factory.sequence(lambda n: n + 1)


class CommentDtoFactory(factory.Factory):
    class Meta:
        model = CommentDto

    comment_id = factory.sequence(lambda n: n + 1)
    comment_content = factory.sequence(lambda n: f" content {n}")
    commented_at = datetime.datetime(2023, 2, 1, 15, 6, 0)
    commented_by_id = factory.sequence(lambda n: n + 1)
    post_id = factory.sequence(lambda n: n + 1)
    parent_comment_id = None


class UserDtoFactory(factory.Factory):
    class Meta:
        model = UserDto

    user_id = factory.sequence(lambda n: n + 1)
    name = factory.Sequence(lambda n: f" user_{n + 1}")
    profile_pic = factory.LazyAttribute(lambda o: f" {o.name}@url")


class ReactionDtoFactory(factory.Factory):
    class Meta:
        model = ReactionDto

    type: factory.Iterator(["HAHA", "WOW", "SAD"])
    post_id: typing.Optional[int] = None
    comment_id: typing.Optional[int] = None
