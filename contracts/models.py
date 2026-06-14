
from django.db import models
from iam.models import Company, User

class ContractTemplate(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='contract_template')
    name = models.CharField(max_length=255)
    body_template = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.company.name})"

class Contract(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'draft', 'Draft'
        SENT = 'sent', 'Sent'
        SIGNED = 'signed', 'Signed'
        ACTIVE = 'active', 'Active'
        CLOSED = 'closed', 'Closed'
        CANCELLED = 'cancelled', 'Cancelled'

    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='contracts')
    template = models.ForeignKey(ContractTemplate, on_delete=models.SET_NULL, null=True, blank=True)
    contractor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contracts')

    contract_number = models.CharField(max_length=50, unique=True)
    subject = models.TextField()
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.DRAFT)

    signed_at = models.DateTimeField(null=True, blank=True)
    file_url = models.URLField(blank=True)
    created_at =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Contract #{self.contract_number}"



