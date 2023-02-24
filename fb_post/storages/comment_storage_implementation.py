import typing
from typing import List, Tuple

from fb_post.interactors.storage_interfaces.dtos import CommentDto, \
    UserDto
from fb_post.models.comment import Comment
from fb_post.interactors.storage_interfaces.comment_storage_interface import \
    CommentStorageInterface


class CommentStorageImplementation(CommentStorageInterface):

    def get_comments_on_post(self, post_id: int) -> List[CommentDto]:
        comments = Comment.objects.filter(post_id=post_id)
        comments_dtos = [
            self._prepare_comment_dto(comment)
            for comment in comments
        ]
        return comments_dtos

    def get_reply_dto(self, parent_comment_ids: List[int]) -> List[CommentDto]:
        replies = Comment.objects.filter(
            parent_comment_id__in=parent_comment_ids)
        replies_post_dtos = [
            self._prepare_reply_dto(reply)
            for reply in replies
        ]
        return replies_post_dtos

    @staticmethod
    def _prepare_reply_dto(reply) -> CommentDto:
        return CommentDto(
            comment_id=reply.id,
            commented_by_id=reply.commented_by_id,
            commented_at=reply.commented_at,
            comment_content=reply.content,
            parent_comment_id=reply.parent_comment_id,
            post_id=None
        )

    @staticmethod
    def _prepare_comment_dto(comment):
        return CommentDto(
            comment_id=comment.id,
            commented_by_id=comment.commented_by_id,
            commented_at=comment.commented_at,
            comment_content=comment.content,
            parent_comment_id=None,
            post_id=comment.post_id
        )
