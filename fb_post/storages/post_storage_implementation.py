from django.db.models import Count

from fb_post.interactors.storage_interfaces.dtos import PostDto
from fb_post.models.post import Post
from fb_post.interactors.storage_interfaces.post_storage_interface import \
    PostStorageInterface


class PostStorageImplementation(PostStorageInterface):
    def create_post(self, user_id: int, post_content: str) -> int:
        post = Post.objects.create(posted_by_id=user_id,
                                   content=post_content)
        return post.id

    def is_post_exists(self, post_id: int) -> bool:
        return Post.objects.filter(id=post_id).exists()

    def get_post_details(self, post_id: int) -> PostDto:
        post = Post.objects.get(id=post_id)
        post_dto = PostDto(
            post_id=post.id,
            posted_at=post.posted_at,
            posted_by_id=post.posted_by_id,
            content=post.content
        )
        return post_dto
