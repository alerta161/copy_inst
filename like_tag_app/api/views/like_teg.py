from rest_framework.mixins import CreateModelMixin, DestroyModelMixin
from rest_framework.viewsets import GenericViewSet

from like_tag_app.api.serializers.like_teg import LikeTegSerializer
from like_tag_app.models import LikeTeg


class LikeTegViewSet(GenericViewSet, CreateModelMixin, DestroyModelMixin):
    serializer_class = LikeTegSerializer
    queryset = LikeTeg.objects.all()