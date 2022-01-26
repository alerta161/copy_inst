from rest_framework import serializers
from like_app.models import Like

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        exclude = ("user", "date" )

    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source="user"
    )