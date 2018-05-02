from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.utils import timezone


class Post(models.Model):
    body = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.body


class Friend(models.Model):
    user = models.ManyToManyField(User)