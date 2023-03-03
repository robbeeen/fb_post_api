from django.db import models
from datetime import datetime


class Post(models.Model):
    content = models.TextField()
    posted_at = models.DateTimeField(default=datetime.now)
    posted_by_id = models.IntegerField(default=1)
