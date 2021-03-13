from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import ModelViewSet

from .models import Project, Todo
from .serializers import ProjectSerializer, TodoSerializer


class ProjectLimitOffsetPagination(LimitOffsetPagination):
    """ Pagination limit. """

    default_limit = 10


class ProjectView(ModelViewSet):
    """Project view."""

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    pagination_class = ProjectLimitOffsetPagination


class TodoView(ModelViewSet):
    """Todo_ view"""

    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
