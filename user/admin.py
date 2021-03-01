from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from . import models

UserAdmin.ordering = ('email',)
UserAdmin.list_display = ('id', 'email', 'first_name', 'middle_name', 'last_name', 'is_staff')
UserAdmin.search_fields = ('first_name', 'middle_name', 'last_name', 'email')
UserAdmin.fieldsets = (
    (None, {'fields': ('password',)}),
    (_('Personal info'), {'fields': ('first_name', 'middle_name', 'last_name', 'email', 'phone')}),
    (_('Permissions'), {
        'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
    }),
    (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
)
UserAdmin.add_fieldsets = (
    (None, {
        'classes': ('wide',),
        'fields': ('password1', 'password2'),
    }),
)

admin.site.register(models.User, UserAdmin)