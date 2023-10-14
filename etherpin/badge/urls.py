from django.urls import include, path
from rest_framework import routers
from etherpin.badge import views

router = routers.DefaultRouter()
router.register(r"badges", views.BadgeViewSet)
router.register(r"badge-ownerships", views.BadgeOwnershipViewSet)
router.register(r"badge-placements", views.BadgePlacementViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
