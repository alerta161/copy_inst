import re

from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save, post_delete, pre_delete

from myweb_main.models import Profile, Post
from tags_app.models import Tag


@receiver(post_save, sender=Post)
def find_or_create_tags(sender, instance, created, *args, **kwargs):
    pattern = re.compile(r'#(\w+)\s?')
    for teg in re.findall(pattern, instance.text):
        tag_instance, tag_is_created = Tag.objects.get_or_create(name=teg)
        tag_instance.posts.add(instance)

