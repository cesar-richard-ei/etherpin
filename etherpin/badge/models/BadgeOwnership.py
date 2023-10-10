from django.db import models


class BadgeOwnership(models.Model):
    """A badge that a user has earned."""

    badge = models.ForeignKey("badge.Badge", on_delete=models.CASCADE)
    user = models.ForeignKey("user.User", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.badge}"
