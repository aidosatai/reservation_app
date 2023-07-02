from rest_framework.routers import DefaultRouter

from users.views import (
    AuthViewSet,
    CustomUserViewSet
)


auth_router = DefaultRouter()
auth_router.register('', AuthViewSet, basename='')

router = DefaultRouter()
router.register('', CustomUserViewSet, basename='users')

urlpatterns = [] + router.urls
