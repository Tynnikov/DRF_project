from rest_framework import serializers

from todoapp.models import Project, Todo


class ProjectSerializer(serializers.ModelSerializer):
    """Project serializer."""

    class Meta:
        model = Project
        fields = '__all__'


class TodoSerializer(serializers.ModelSerializer):
    """Todo_ serializer."""

    class Meta:
        model = Todo
        fields = '__all__'
