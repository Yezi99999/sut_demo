from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'phone', 'role', 'is_staff', 'is_active')
    list_filter = ('role', 'is_staff', 'is_active')
    fieldsets = UserAdmin.fieldsets + (
        ('额外信息', {'fields': ('phone', 'avatar', 'role')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('额外信息', {'fields': ('email', 'phone', 'avatar', 'role')}),
    )