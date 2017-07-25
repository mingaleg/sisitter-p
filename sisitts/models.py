from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Sisit(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, related_name='own_sisits')
    likes_count = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)

    likes = models.ManyToManyField(User, related_name='liked_sisits')

    def __str__(self):
        return "{}: {}".format(
            self.author,
            self.content[:32],
        )

    def get_likes_count(self):
        return self.likes.count()
