from typing import List

from django.db.models import Count, Q

from fb_post.constants.enums import Sort
from fb_post.exceptions.custom_exceptions import InvalidPostException
from fb_post.interactors.storage_interfaces.dtos import PostDto, \
    GetPostParametersDto
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

        is_post_not_exists = not self.is_post_exists(post_id)
        if is_post_not_exists:
            raise InvalidPostException
        else:
            post = Post.objects.get(id=post_id)
            post_dto = PostDto(
                post_id=post.id,
                posted_at=post.posted_at,
                posted_by_id=post.posted_by_id,
                content=post.content

            )
            return post_dto

    def get_all_post_ids(self,
                         get_post_parameters_dto: GetPostParametersDto) -> \
            List[int]:
        limit = get_post_parameters_dto.limit
        sortby = get_post_parameters_dto.sortby
        offset = get_post_parameters_dto.offset
        filterby = get_post_parameters_dto.filterby
        sortby_order = get_post_parameters_dto.sortby_order

        if sortby == Sort.ID.value:
            if filterby:
                if sortby_order == "ASC" or sortby_order == "asc":
                    posts = Post.objects.filter(
                        content__icontains=filterby).order_by('id')
                else:
                    posts = Post.objects.filter(
                        content__icontains=filterby).order_by('-id')
            else:
                if sortby_order == "ASC" or sortby_order == "asc":
                    posts = Post.objects.all().order_by('id')
                else:
                    posts = Post.objects.all().order_by('-id')

        elif sortby == Sort.POSTED_AT.value:
            if filterby:
                if sortby_order == "ASC" or sortby_order == "asc":
                    posts = Post.objects.filter(
                        content__icontains=filterby).order_by('posted_at')
                else:
                    posts = Post.objects.filter(
                        content__icontains=filterby).order_by('-posted_at')
            else:
                if sortby_order == "ASC" or sortby_order == "asc":
                    posts = Post.objects.all().order_by('posted_at')
                else:
                    posts = Post.objects.all().order_by('-posted_at')

        else:
            if filterby:
                posts = Post.objects.filter(Q(content__icontains=filterby))
            else:
                posts = Post.objects.all()
        print(posts)
        total_post = posts.count()
        if total_post > offset + limit:
            posts = posts[offset:offset + limit]
        else:
            posts = posts[0:offset + limit]
        post_ids = list(post.id for post in posts)
        return post_ids
