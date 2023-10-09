from django.contrib.auth.models import AbstractUser
from django.db import models
from django.dispatch import receiver
from allauth.account.signals import user_logged_in


class User(AbstractUser):
    last_name: str = models.CharField(max_length=255)
    first_name: str = models.CharField(max_length=255)

    @receiver(user_logged_in)
    def populate_profile(sociallogin, user, **kwargs):
        if sociallogin.account.provider == "github":
            user_data = user.socialaccount_set.filter(provider="github")[
                0
            ].extra_data  # noqa E501
            if user_data["login"] in ("cesar-richard", "mael-belval"):
                user.is_staff = True
                user.is_superuser = True
                user.save()
