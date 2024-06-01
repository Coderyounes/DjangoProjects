from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    article = models.ForeignKey('posts.Posts', on_delete=models.CASCADE, default=1)
    content = models.CharField(max_length=700)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        pass

    def __str__(self):
        return f"Comment from {self.user.username}"
