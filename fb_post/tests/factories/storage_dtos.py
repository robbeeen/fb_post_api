import datetime
import factory
import typing

from fb_post.constants.enums import ReactionENUM
from fb_post.interactors.storage_interfaces.dtos import CommentDto, PostDto, \
    ReactionDto, GetPostParametersDto


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


class ReactionDtoFactory(factory.Factory):
    class Meta:
        model = ReactionDto

    type = "HAHA"
    post_id: typing.Optional[int] = None
    comment_id: typing.Optional[int] = None


class GetPostParametersDtoFactory(factory.Factory):
    class Meta:
        model = GetPostParametersDto

    offset = 0
    limit = 5
    sortby: None
    filterby: None
    sortby_order: None
