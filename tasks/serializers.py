from rest_framework import serializers
from tasks.models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'id', 'company', 'created_by', 'assigned_to', 'contract',
            'title', 'description', 'budget', 'deadline', 'status', 'created_at',
        ]
        read_only_fields = ['id', 'company', 'created_by', 'assigned_to', 'contract', 'status', 'created_at']


class TaskCreateSerializer(serializers.Serializer):
    """Create task by admin"""
    title = serializers.CharField(max_length=255)
    description = serializers.CharField()
    budget = serializers.DecimalField(max_digits=12, decimal_places=2)
    deadline = serializers.DateTimeField(required=False, allow_null=True)
    assigned_to_id = serializers.IntegerField(required=False, allow_null=True)