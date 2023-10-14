from rest_framework import serializers
from etherpin.badge.models import Badge


class BadgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Badge
        fields = (
            "id",
            "title",
            "description",
            "image",
            "creator",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("created_at", "updated_at")
