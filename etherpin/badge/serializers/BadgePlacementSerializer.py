from rest_framework import serializers
from etherpin.badge.models import BadgePlacement


class BadgePlacementSerializer(serializers.ModelSerializer):
    class Meta:
        model = BadgePlacement
        fields = (
            "id",
            "badge_ownership",
            "x",
            "y",
            "size",
            "rotation",
            "created_at",
        )
        read_only_fields = ("id", "created_at")
