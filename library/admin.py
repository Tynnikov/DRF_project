from django.contrib import admin

from . import models


@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    list_display_links = ('first_name', 'last_name')
