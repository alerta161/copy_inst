"""myweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from drf_spectacular.views import SpectacularRedocView, SpectacularSwaggerView, SpectacularAPIView
from myweb_main.api.router import api_router as myweb_main_router
from media_app.api.router import api_router as media_router
from like_app.api.router import api_router as like_router
from tags_app.api.router import api_router as tags_router
from comment_app.api.router import api_router as comment_router
from like_tag_app.api.router import api_router as like_teg_router
from like_comment_app.api.router import api_router as like_comment_router
from followers_app.api.router import api_router as followers_router
from myweb_main.views import reg_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myweb_main.urls')),
    path('reg/', reg_page, name="reg"),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('api/swagger/', SpectacularSwaggerView.as_view(), name='swagger-ui'),
    path('api/', include(myweb_main_router.urls)),
    path("api/", include(media_router.urls)),
    path("api/", include(tags_router.urls)),
    path("api/", include(like_router.urls)),
    path("api/", include(comment_router.urls)),
    path("api/", include(like_teg_router.urls)),
    path("api/", include(like_comment_router.urls)),
    path("api/", include(followers_router.urls)),
   ]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()