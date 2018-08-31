from django.conf.urls import include, url
from rest_framework import routers

from posts.views import PostViewSet

router = routers.DefaultRouter(trailing_slash=False)

router.register(r'posts', PostViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
]