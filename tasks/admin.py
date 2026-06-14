from django.contrib import admin

from tasks.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'company', 'created_by', 'assigned_to', 'status', 'budget')
    list_filter = ('status', 'company')