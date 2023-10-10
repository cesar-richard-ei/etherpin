from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/doc/", include("django.contrib.admindocs.urls")),
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("api/badges/", include("etherpin.badge.urls")),
    path("api/users/", include("etherpin.user.urls")),
    path("", include("etherpin.user.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
