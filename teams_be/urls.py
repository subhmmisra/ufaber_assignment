from django.contrib import admin
from django.urls import path, include

from teams_be.frontend import urls
from teams_be import api_urls, frontend

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include(api_urls)),
    path('', include(frontend.urls)),
]





