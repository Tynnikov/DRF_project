from rest_framework.viewsets import ModelViewSet
from .models import Project, Todo
from .serializers import ProjectSerializer, TodoSerializer

class ProjectView(ModelViewSet):
    """Project view."""

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class TodoView(ModelViewSet):
    """Todo_ view"""

    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
