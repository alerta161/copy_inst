from django.db import models
from django.contrib.auth.models import User

from myweb_main.models import Post


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, related_name='likes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=False, blank=False, related_name='likes')
    date = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        unique_together = (("user", "post"), )
