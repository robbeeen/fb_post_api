from django.db import models
from .user import User
from datetime import datetime
from .post import Post


class Comment(models.Model):
    content = models.TextField()
    commented_at = models.DateTimeField(default=datetime.now())
    commented_by = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True,
                             null=True, )
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE,
                                       blank=True, null=True, )
