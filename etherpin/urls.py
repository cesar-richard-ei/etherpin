from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from etherpin.user.views import home
from rest_framework import routers

router = routers.DefaultRouter()
router.routes.append(
    [
        path("badges/", include("etherpin.badge.urls")),
        path("users/", include("etherpin.user.urls")),
    ]
)

urlpatterns = [
    path("admin/doc/", include("django.contrib.admindocs.urls")),
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("api/", include(router.urls)),
    path("", home, name="Home"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
