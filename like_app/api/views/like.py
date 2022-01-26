from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet

from like_app.api.serializers.like import LikeSerializer
from like_app.models import Like


class LikeViewSet(GenericViewSet, CreateModelMixin, DestroyModelMixin, ListModelMixin):
    serializer_class = LikeSerializer
    queryset = Like.objects.all()


