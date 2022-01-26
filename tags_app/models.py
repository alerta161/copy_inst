from django.db import models

from myweb_main.models import Post


class Tag(models.Model):
    name = models.CharField(max_length=1024, null=False, unique=True)
    posts = models.ManyToManyField(Post, related_name='tags')
