from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea
from .models import User
from django.db import models


class UserAdminConfig(UserAdmin):
    model = User
    search_fields = ('email', 'username',)
    list_filter = ('email', 'username', 'is_active', 'is_teacher')
    ordering = ('-date_joined',)
    list_display = ('email', 'username', 'is_active', 'is_teacher')
    fieldsets = (
        ('Authentication Details', {'fields': ('email', 'username', 'is_teacher')}),
        ('Personal Details', {'fields': ('first_name', 'last_name', 'date_of_birth')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'is_active', 'is_teacher')}
         ),
    )
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 20, 'cols': 60})},
        models.CharField: {'widget': TextInput(attrs={'size': 20})},
    }


admin.site.register(User, UserAdminConfig)