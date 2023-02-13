from django.db import models
from datetime import datetime
from .user import User


class Post(models.Model):
    content = models.TextField()
    posted_at = models.DateTimeField(default=datetime.now)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
