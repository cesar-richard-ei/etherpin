from django.shortcuts import render
from .UserViewSet import UserViewSet


def home(request):
    return render(request, "home.html")


__all__ = ["UserViewSet", "home"]
