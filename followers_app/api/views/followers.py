from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, ListModelMixin, DestroyModelMixin
from rest_framework.viewsets import GenericViewSet

from followers_app.api.serializers.followers import FollowersSerializer
from followers_app.models import Followers


class FollowersViewSet(GenericViewSet, CreateModelMixin, RetrieveModelMixin, ListModelMixin, DestroyModelMixin):
    serializer_class = FollowersSerializer
    queryset = Followers.objects.all()