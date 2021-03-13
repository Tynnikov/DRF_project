from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from .filters import ProjectFilters, TodoFilters
from .models import Project, Todo
from .serializers import ProjectSerializer, TodoSerializer


class ProjectLimitOffsetPagination(LimitOffsetPagination):
    """ Pagination limit. """

    default_limit = 10


class ProjectViewSet(ModelViewSet):
    """ Project view (CRUD) with pagination and filters. """

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    pagination_class = ProjectLimitOffsetPagination
    filterset_class = ProjectFilters


class TodoLimitOffsetPagination(LimitOffsetPagination):
    """ Todo_ limit. """

    default_limit = 20


class TodoView(ModelViewSet):
    """ Todo_ view (CRUD) with pagination and filters. """

    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    pagination_class = TodoLimitOffsetPagination
    filterset_class = TodoFilters

    def destroy(self, request, *args, **kwargs):
        """ Projects that have been deleted get the flag removed. """
        to_do = self.get_object()
        to_do.is_removed = True
        to_do.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
