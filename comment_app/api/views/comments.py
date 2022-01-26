from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet

from comment_app.api.serializers.comments import CommentSerializer
from comment_app.models import Comment


class CommentViewSet(GenericViewSet, CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, ListModelMixin):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
