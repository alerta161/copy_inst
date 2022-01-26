from rest_framework import routers

from like_tag_app.api.views.like_teg import LikeTegViewSet

api_router = routers.DefaultRouter()

api_router.register('like_teg', LikeTegViewSet)