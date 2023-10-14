from rest_framework import serializers
from etherpin.badge.models import BadgeOwnership


class BadgeOwnershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = BadgeOwnership
        fields = ("id", "badge", "user", "created_at", "updated_at")
        read_only_fields = ("id", "created_at", "updated_at")
