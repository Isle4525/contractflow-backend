from django.db import models

from contracts.models import Contract
from iam.models import Company,User


class Task(models.Model):
    class Status(models.TextChoices):
        CREATED = 'created', 'Created'
        ACCEPTED = 'accepted', 'Accepted'
        IN_PROGRESS = 'in_progress', 'In Progress'
        SUBMITTED = 'submitted', 'Submitted'
        REVIEW = 'review', 'In Review'
        APPROVED = 'approved', 'Approved'
        REJECTED = 'rejected', 'Rejected'
        COMPLETED = 'completed', 'Completed'

    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='tasks')
    created_by = models.ForeignKey(User,on_delete=models.CASCADE, related_name='created_task')
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_tasks')
    contract = models.OneToOneField(Contract, on_delete=models.SET_NULL, null=True, blank=True, related_name='task')
    title = models.CharField(max_length=255)
    description = models.TextField()
    budget = models.DecimalField(max_digits=12, decimal_places=2)
    deadline = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.CREATED)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Tasks #{self.id}: {self.title}"