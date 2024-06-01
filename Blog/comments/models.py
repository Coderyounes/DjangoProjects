from django.db import models


class Comments(models.Model):
    name = models.CharField(max_length=30)
    content = models.CharField(max_length=200)
    created_at = ""

