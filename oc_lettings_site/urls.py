from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from . import views

handler404 = views.page_not_found
handler500 = views.server_error


def trigger_error(request):
    division_by_zero = 1/0
    return division_by_zero


urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include('lettings.urls')),
    path('profiles/', include('profiles.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns.append(path('sentry-debug/', trigger_error))
