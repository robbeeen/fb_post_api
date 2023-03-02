# your django admin
from django.contrib import admin
from fb_post.models.post import Post
from fb_post.models.reaction import Reaction
from fb_post.models.comment import Comment

admin.site.register(Post)
admin.site.register(Reaction)
admin.site.register(Comment)
