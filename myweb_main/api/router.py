from rest_framework import routers

from myweb_main.api.views.myweb_main import PostsView

api_router = routers.DefaultRouter()

api_router.register('post', PostsView)
