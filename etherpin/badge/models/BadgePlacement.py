from django.db import models
from django.core.validators import MaxValueValidator


class BadgePlacement(models.Model):
    """A badge position on the user's board."""

    badge_ownership = models.ForeignKey(
        "badge.BadgeOwnership", on_delete=models.CASCADE
    )
    user = models.ForeignKey("user.User", on_delete=models.CASCADE)
    x = models.PositiveSmallIntegerField(default=0)
    y = models.PositiveSmallIntegerField(default=0)
    size = models.PositiveSmallIntegerField(default=100)
    rotation = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(360)], default=0
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.badge}"
