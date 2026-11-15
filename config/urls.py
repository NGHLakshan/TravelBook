"""
URL configuration for config project.
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core.views import home_view, code_lookup_view, search_api_view, github_webhook_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('lookup/', code_lookup_view, name='code_lookup'),
    path('api/search/', search_api_view, name='search_api'),
    path('git-update/', github_webhook_view, name='github_webhook'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT if hasattr(settings, 'STATIC_ROOT') else None)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
