from django.db import models
from .user import User
from datetime import datetime
from .comment import Comment
from .post import Post


class Reaction(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True,
                             blank=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True,
                                blank=True)
    reaction = models.CharField(max_length=100)
    reacted_at = models.DateTimeField(default=datetime.now)
    reacted_by = models.ForeignKey(User, on_delete=models.CASCADE)
