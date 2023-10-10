from django.db import models


class Badge(models.Model):
    """A badge that can be earned by a user."""

    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="badges")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
