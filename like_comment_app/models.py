from django.db import models
from django.contrib.auth.models import User

from comment_app.models import Comment


class LikeComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, related_name='likes_comment')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=False, blank=False, related_name='likes_comment')

    class Meta:
        unique_together = (("user", "comment"), )

