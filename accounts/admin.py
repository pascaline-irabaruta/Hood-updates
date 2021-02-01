from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.

class CustomUserAdmin(UserAdmin):

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('avatar','bio', 'neighbourhood')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('avatar','bio')}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
