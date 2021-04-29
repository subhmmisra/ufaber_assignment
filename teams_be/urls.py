from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.views.static import serve

from teams_be.frontend import urls
from teams_be import api_urls, frontend

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include(api_urls)),
    path('', include(frontend.urls)),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]





