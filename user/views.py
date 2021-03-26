from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from .models import User
from .serializers import UserSerializer


class UserRegistrationView(ModelViewSet):
    """ User registration without authentication. """

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserProfileView(RetrieveUpdateAPIView):
    """ Retrieve and update user profile with permission. """

    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = User.objects.all()
    serializer_class = UserSerializer
