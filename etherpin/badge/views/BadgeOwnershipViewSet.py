from rest_framework import viewsets, permissions
from etherpin.badge.models import BadgeOwnership
from etherpin.badge.serializers import BadgeOwnershipSerializer


class BadgeOwnershipViewSet(viewsets.ModelViewSet):
    queryset = BadgeOwnership.objects.all()
    serializer_class = BadgeOwnershipSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
