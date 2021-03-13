from django_filters import rest_framework as filters
from .models import Project


class ProjectFilters(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Project
        fields = ['title']
