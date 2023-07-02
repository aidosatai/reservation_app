from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings

from users.urls import auth_router

api_patterns = [
    path('auth/', include(auth_router.urls)),
    path('users/', include('users.urls')),
    path('rooms/', include('rooms.urls')),
    path('booking/', include('bookings.urls')),
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(api_patterns))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + \
              static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
