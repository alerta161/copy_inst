from rest_framework import serializers
from like_tag_app.models import LikeTeg

class LikeTegSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeTeg
        exclude = ("user", )

    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source="user"
    )