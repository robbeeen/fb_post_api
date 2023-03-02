from django.db import models
from datetime import datetime
from .post import Post


class Comment(models.Model):
    content = models.TextField()
    commented_at = models.DateTimeField(default=datetime.now)
    commented_by_id = models.IntegerField(default=1)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True,
                             null=True, )
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE,
                                       blank=True, null=True, )
