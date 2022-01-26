from rest_framework import routers

from followers_app.api.views.followers import FollowersViewSet

api_router = routers.DefaultRouter()

api_router.register('followers', FollowersViewSet)