from rest_framework import viewsets, permissions
from etherpin.badge.models import BadgePlacement
from etherpin.badge.serializers import BadgePlacementSerializer


class BadgePlacementViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows badge placements to be viewed or edited.
    """

    queryset = BadgePlacement.objects.all()
    serializer_class = BadgePlacementSerializer
    permission_classes = [permissions.IsAuthenticated]
