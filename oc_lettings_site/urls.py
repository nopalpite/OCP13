from django.contrib import admin
from django.urls import path, include

from . import views

handler404 = views.page_not_found
handler500 = views.server_error

urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include('lettings.urls')),
    path('profiles/', include('profiles.urls')),
    path('admin/', admin.site.urls),
]
