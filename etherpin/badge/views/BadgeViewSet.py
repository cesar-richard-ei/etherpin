from rest_framework import viewsets, permissions
from etherpin.badge.models import Badge
from etherpin.badge.serializers import BadgeSerializer


class BadgeViewSet(viewsets.ModelViewSet):
    queryset = Badge.objects.all()
    serializer_class = BadgeSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
