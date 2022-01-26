from rest_framework import routers

from like_comment_app.api.views.like_comment import LikeCommentViewSet

api_router = routers.DefaultRouter()

api_router.register('like_comment', LikeCommentViewSet)