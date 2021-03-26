from uuid import uuid4

from django.db import models

from tools.models import BaseUpdatableModel
from user.models import User


class Project(BaseUpdatableModel):
    uuid = models.UUIDField(primary_key=True, default=uuid4)
    title = models.CharField(max_length=300, blank=True, null=True)
    users = models.ManyToManyField(User)
    repository = models.URLField(blank=True, null=True)

    def __str__(self):
        return f'{self.title} {self.users} {self.repository}'


class Todo(BaseUpdatableModel):
    uuid = models.UUIDField(primary_key=True, default=uuid4)
    project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='project', null=True)
    text = models.TextField()
    is_active = models.BooleanField(default=True)
