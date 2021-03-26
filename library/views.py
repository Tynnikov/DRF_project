from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import ModelViewSet

from .models import Author
from .serializers import AuthorModelSerializer


class AuthorModelViewSet(ModelViewSet):
    """Display all Authors."""

    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer


class AuthorLimitOffsetPagination(LimitOffsetPagination):
    """ Pagination limit. """

    default_limit = 3


class AuthorLimitOffsetPaginationViewSet(ModelViewSet):
    """Display all Authors with pagination."""

    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer
    pagination_class = AuthorLimitOffsetPagination
