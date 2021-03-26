from django.contrib import admin

from . import models


@admin.register(models.Todo)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'project')
    list_display_links = ('project',)



@admin.register(models.Project)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'title', 'repository')
    list_display_links = ('uuid', 'title')
