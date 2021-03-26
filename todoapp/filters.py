from django_filters import rest_framework as filters
from .models import Project, Todo


class ProjectFilters(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Project
        fields = ['title']


class TodoFilters(filters.FilterSet):
    todo_project = filters.CharFilter(lookup_expr='icontains')
    created_year = filters.NumberFilter(field_name='created_at', lookup_expr='year')
    date_between = filters.DateFromToRangeFilter(field_name="created_at", label="Date (Between)")

    class Meta:
        model = Todo
        fields = ['todo_project']
