from django.contrib import admin
from etherpin.badge.models import Badge, BadgeOwnership, BadgePlacement


@admin.register(Badge)
class BadgeAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "image", "is_active")
    list_filter = ("is_active",)
    search_fields = ("title", "description")
    ordering = ("title",)
    readonly_fields = ("created_at", "updated_at")


@admin.register(BadgeOwnership)
class BadgeOwnershipAdmin(admin.ModelAdmin):
    list_display = ("badge", "user")
    # list_filter = ("is_active",)
    search_fields = ("badge", "user")
    ordering = ("badge", "user")


@admin.register(BadgePlacement)
class BadgePlacementAdmin(admin.ModelAdmin):
    pass
