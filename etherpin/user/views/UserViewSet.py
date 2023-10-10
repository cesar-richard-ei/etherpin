from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from etherpin.user.models import User
from etherpin.user.serializers import UserSerializer
from rest_framework.exceptions import PermissionDenied


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)

    def get_permissions(self):
        if self.action == "create":
            return [AllowAny()]
        return super().get_permissions()

    def list(self, request, *args, **kwargs):
        """
        Returns a list of all users.
        """
        if not request.user.is_superuser:
            raise PermissionDenied(
                {"message": "You are not allowed to list all users."}
            )
        return super().list(request, *args, **kwargs)

    @action(detail=False, methods=["get"])
    def me(self, request):
        """
        Returns the currently logged in user.
        """
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
