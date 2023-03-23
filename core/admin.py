"""
Django admin customizaion.
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from core import models

class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users."""
    ordering =['id']
    list_display = ['email','name']
    fieldsets = (
        (None,{'fields': ('email','password')}),
        (
            _('Permissions'),
            {
                'fields' : (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            }
        ),
        (_('Importtant dates hello'),{'fields' : ('last_login',)}),
    )
    readonly_fields = ['last_login']
    add_fieldsets = (
        (None,{
            'classes': ('wide',),
            'fields': (
                'email',
                'password1',
                'password2',
                'name',
                'is_active',
                'is_staff',
                'is_superuser',
            )
        }),
    )


<<<<<<< HEAD
admin.site.register(models.User,UserAdmin)
=======
admin.site.register(models.User,UserAdmin)
>>>>>>> 1e18a8600c52a1323b6613e527b04a875c898382
