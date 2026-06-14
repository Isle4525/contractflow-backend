from django.utils import timezone
from .models import Contract

def generate_contract_number(company_id: int) -> str:
    """CMP{company_id}-{year}-{seq}"""
    year = timezone.now().year
    count = Contract.objects.filter(
        company_id=company_id,
        created_at__year=year
    ).count()

    return f"CMP{company_id}-{year}-{count + 1:04d}"