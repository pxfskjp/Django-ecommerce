from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import ugettext_lazy as _

from . import models


class UserAdmin(BaseUserAdmin):
    list_display = ('email', 'is_active', 'is_staff',)
    ordering = ('email',)
    search_fields = ('email',)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )

    fieldsets = (
        (None, {
            'fields': ('email', 'password')
        }),
        (_('Permissions'), {
            'fields': (
                ('is_active', 'is_staff', 'is_superuser',),
                'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login',)}),
    )


admin.site.register(models.User, UserAdmin)
