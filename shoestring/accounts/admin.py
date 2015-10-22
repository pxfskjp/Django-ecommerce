from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from . import models


class UserAdmin(BaseUserAdmin):
    list_display = ('email', 'is_active', 'is_staff',)
    list_filter = ('is_active', 'is_staff',)
    ordering = ('email',)

admin.site.register(models.User, UserAdmin)
