import typing
from dataclasses import dataclass
from typing import List


@dataclass()
class ReactionDto:
    type: str
    post_id: typing.Optional[int] = None
    comment_id: typing.Optional[int] = None


@dataclass()
class CommentDto:
    comment_id: int
    commented_by_id: int
    commented_at: str
    comment_content: str
    post_id: typing.Optional[int] = None
    parent_comment_id: typing.Optional[int] = None


@dataclass
class PostDto:
    post_id: int
    posted_by_id: int
    posted_at: str
    content: str


@dataclass
class GetPostParametersDto:
    offset: int
    limit: int
    sortby: typing.Any
    filterby: str
    sortby_order: str
