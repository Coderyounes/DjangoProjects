from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Posts(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        pass

    def __str__(self):
        return f"Post by {self.user.username}"
