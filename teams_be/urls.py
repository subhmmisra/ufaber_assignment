from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from teams_be.frontend import urls
from teams_be import api_urls, frontend
from .base import views as base_views

handler500 = base_views.server_error

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include(api_urls)),
    path('', include(frontend.urls)),
    path("500/", handler500),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)





