from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet,PostViewSet,LikeViewSet


router = DefaultRouter()
router.register(r'user', UserViewSet, basename="user")
router.register(r'post', PostViewSet, basename="post")
router.register(r'like', LikeViewSet, basename="like")

urlpatterns = [
    path("", include(router.urls))
]