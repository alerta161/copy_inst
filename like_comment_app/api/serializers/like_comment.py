from rest_framework import serializers
from like_comment_app.models import LikeComment

class LikeCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeComment
        exclude = ("user", )

    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source="user"
    )
