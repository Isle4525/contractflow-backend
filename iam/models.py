from django.db import models
from django.contrib.auth.models import AbstractUser

class Company(models.Model):
    name = models.CharField(max_length=255)
    bin = models.CharField(max_length=12, blank=True)
    requisites = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = 'admin', 'Admin'
        MANAGER = 'manager', 'Manager'
        ACCOUNTANT = 'accountant', 'Accountant'
        CONTRACTOR = 'contractor', 'Contractor'

    role = models.CharField(max_length=20, choices=Role.choices)
    company = models.ForeignKey(Company, null=True, blank=True, on_delete=models.CASCADE, related_name='users')
    is_self_employed = models.BooleanField(default=False)

    def __str__(self):
        return self.username