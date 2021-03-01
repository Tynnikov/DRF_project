from rest_framework.viewsets import ModelViewSet

from .models import User
from .serializers import UserSerializer


class UserRegistrationView(ModelViewSet):
    """ User registration. """

    queryset = User.objects.all()
    serializer_class = UserSerializer
