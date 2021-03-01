from rest_framework.viewsets import ModelViewSet

from .models import Author
from .serializers import AuthorModelSerializer


class AuthorModelViewSet(ModelViewSet):
    """Display all Authors."""

    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer
