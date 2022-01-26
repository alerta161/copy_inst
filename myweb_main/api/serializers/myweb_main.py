from rest_framework import serializers

from media_app.api.serializers.media import MediaSerializer
from myweb_main.models import Post
from tags_app.api.serializers.tag import TagSerializer


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        read_only_fields = ['id', 'user', 'image']
        exclude = ['is_public']
        extra_kwargs = {
            'file': {"required": True, 'write_only': True, 'help_text': 'ID Медиа Файла', }
        }

    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source="user"
    )
    media = MediaSerializer(source='file', allow_null=True, read_only=True )
    tags = TagSerializer(many=True, read_only=True)

    likes_count = serializers.SerializerMethodField()

    def get_likes_count(self, instance) -> int:
        return instance.likes.count()

    comments_count = serializers.SerializerMethodField()

    def get_comments_count(self, instance) -> int:
        return instance.comments.count()
