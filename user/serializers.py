from rest_framework import serializers

from user.models import User


class UserSerializer(serializers.ModelSerializer):
    """User serializer."""

    password = serializers.CharField(max_length=500, write_only=True)

    class Meta:
        model = User
        fields = ['id', 'nick_name', 'first_name', 'last_name', 'email', 'password']
        read_only_fields = ['id']
        extra_kwargs = {'password': {'write_only': True}}
