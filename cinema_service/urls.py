from debug_toolbar.toolbar import debug_toolbar_urls
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/cinema/", include("cinema.urls"), name="cinema"),
] + debug_toolbar_urls()
