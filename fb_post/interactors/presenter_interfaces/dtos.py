from dataclasses import dataclass
from typing import List

from fb_post.adapters.fb_post_auth_adapter import UserDto
from fb_post.interactors.storage_interfaces.dtos import PostDto,CommentDto, ReactionDto


@dataclass()
class GetPostResponseDto:
    post_dto: PostDto
    user_dtos: List[UserDto]
    comment_dtos: List[CommentDto]
    reply_dtos: List[CommentDto]
    reactions_on_post_dtos: List[ReactionDto]
    reactions_on_comments_dtos: List[ReactionDto]
