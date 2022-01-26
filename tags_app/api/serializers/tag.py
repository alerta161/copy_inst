from rest_framework import serializers

from tags_app.models import Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        exclude = [
            "posts",
        ]

    posts_count = serializers.SerializerMethodField()

    def get_posts_count(self, instance) -> int:
        return instance.posts.count()

    likes_teg_count = serializers.SerializerMethodField()

    def get_likes_teg_count(self, instance) -> int:
        return instance.likes_teg.count()

class TagDetailSerializer(TagSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


