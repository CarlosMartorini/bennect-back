from rest_framework import viewsets
from accounts.serializers import UserSerializer
from accounts.models import User


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
