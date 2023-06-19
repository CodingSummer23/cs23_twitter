from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Tweet(models.Model):
    content = models.CharField(max_length=140)
    published_on = models.DateTimeField(default=datetime.now())
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.content
