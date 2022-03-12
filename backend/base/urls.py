from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.contrib.staticfiles.views import serve
from django.views.decorators.cache import never_cache


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('post.urls', namespace='post'))
]

if settings.DEBUG:
    urlpatterns.append(path('__debug__/', include('debug_toolbar.urls')))
    urlpatterns.append(path('static/<path:path>', never_cache(serve)))
