from django.db import models
from django.contrib.auth.models import User

from tags_app.models import Tag


class LikeTeg(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, related_name='likes_teg')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, null=False, blank=False, related_name='likes_teg')

    class Meta:
        unique_together = (("user", "tag"), )
