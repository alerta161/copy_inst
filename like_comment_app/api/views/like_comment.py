from rest_framework.mixins import CreateModelMixin, DestroyModelMixin
from rest_framework.viewsets import GenericViewSet

from like_comment_app.api.serializers.like_comment import LikeCommentSerializer
from like_comment_app.models import LikeComment


class LikeCommentViewSet(GenericViewSet, CreateModelMixin, DestroyModelMixin):
    serializer_class = LikeCommentSerializer
    queryset = LikeComment.objects.all()