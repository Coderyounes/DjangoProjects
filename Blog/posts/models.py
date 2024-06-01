from django.db import models


class Posts(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    # TODO: Define FK
