from django.db import models


class Badge(models.Model):
    """A badge that can be earned by a user."""

    title = models.CharField(max_length=255)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    creator = models.ForeignKey(
        "user.User", on_delete=models.CASCADE, related_name="badges_created"
    )
    image = models.ImageField(upload_to="badges")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
