from fb_post.models.post import Post
from fb_post.interactors.storage_interfaces.post_storage_interface import \
    PostStorageInterface


class PostStorageImplementation(PostStorageInterface):
    def create_post(self, user_id: int, post_content: str) -> int:
        post = Post.objects.create(posted_by_id=user_id,
                                   content=post_content)
        return post.id
