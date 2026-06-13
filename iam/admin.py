from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from iam.models import Company, User


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'bin', 'created_at')

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'username', 'email', 'role', 'company', 'is_self_employed')
    fieldsets = UserAdmin.fieldsets + (
        ('Extra', {'fields': ('role', 'company', 'is_self_employed')}),
    )