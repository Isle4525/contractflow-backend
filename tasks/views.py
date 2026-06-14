from django.db.migrations import serializer
from django.shortcuts import render
from django.db.models import Q, Model
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError as DRFValidationError
from .services import accept_task

import tasks
from iam.models import User
from tasks.models import Task
from tasks.serializers import TaskSerializer, TaskCreateSerializer


class TaskAcceptView(APIView):
    """POST /api/tasks/{id}/accept/"""
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, id):
        user = request.user
        if user.role != User.Role.CONTRACTOR:
            raise PermissionDenied("Only contractors can accept tasks")

        task = get_object_or_404(Task, id=id)

        try:
            task = accept_task(task,user)
        except ValueError as e:
            raise DRFValidationError(str(e))

        return Response(TaskSerializer(task).data)


class TaskListCreateView(generics.ListCreateAPIView):
    """GET/POST /api/tasks/"""
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == User.Role.CONTRACTOR:
            return Task.objects.filter(Q(assigned_to=user) | Q(assigned_to__isnull=True, status=Task.Status.CREATED))

        return Task.objects.filter(company=user.company)


    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TaskCreateSerializer
        return TaskSerializer


    def create(self, request, *args, **kwargs):
        user = request.user
        if user.role == User.Role.CONTRACTOR:
            raise PermissionDenied("Contractor cannot create tasks")

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        assigned_to = None
        if data.get('assigned_ti_id'):
            assigned_to = get_object_or_404(User, id=data['assigned_to_id'], role=User.Role.CONTRACTOR)

        task = Task.objects.create(
            company=user.company,
            created_by=user,
            assigned_to=assigned_to,
            title=data['title'],
            description=data['description'],
            budget=data['budget'],
            deadline=data.get('deadline'),
        )

        return Response(TaskSerializer(task).data, status=status.HTTP_201_CREATED)

class TaskDetailView(generics.RetrieveAPIView):
    """GET /api/tasks/{id}/"""
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        user = self.request.user
        if user.role == User.Role.CONTRACTOR:
            return Task.objects.filter(Q(assigned_to=user) | Q(assigned_to__isnull=True, status=Task.Status.CREATED))

        return Task.objects.filter(company=user.company)