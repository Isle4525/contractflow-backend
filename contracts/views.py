from django.utils import timezone
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied, ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView
from iam.models import User
from .models import Contract, ContractTemplate
from .serializers import ContractSerializer, ContractCreateSerializer, ContractTemplateSerializer
from .services import generate_contract_number


class ContractTemplateListCreateView(generics.ListCreateAPIView):
    """GET/POST /api/contracts/templates"""
    serializer_class = ContractTemplateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return ContractTemplate.objects.filter(company=self.request.user.company)

    def perform_create(self, serializer):
        serializer.save(company=self.request.user.company)


class ContractListCreateView(generics.ListCreateAPIView):
    """GET/POST /api/contracts/"""
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == User.Role.CONTRACTOR:
            return Contract.objects.filter(contractor=user)
        return Contract.objects.filter(company=user.company)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ContractCreateSerializer
        return ContractSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        company = request.user.company
        contractor = User.objects.get(id=data['contractor_id'], role=User.Role.CONTRACTOR)

        contract = Contract.objects.create(
            company=company,
            template_id=data.get('template_id'),
            contractor=contractor,
            contract_number=generate_contract_number(company.id),
            subject=data['subject'],
            amount=data['amount'],
        )
        return Response(ContractSerializer(contract).data, status=201)

class ContractSignView(APIView):
    """POST /api/contracts/{id}/sign/"""
    permission_classes = [permissions.IsAuthenticated]

    def post(self, requset, id):
        contract = get_object_or_404(Contract, id=id)

        if contract.contractor_id != requset.user.id:
            raise PermissionDenied("You can only sign your own contracts")

        if contract.status != Contract.Status.DRAFT and contract.status != Contract.Status.SENT:
            raise ValidationError(f"Cannot sign contract with status '{contract.status}'")

        contract.status = Contract.Status.SIGNED
        contract.signed_at = timezone.now()
        contract.save()

        return Response(ContractSerializer(contract).data)

class ContractDetailView(generics.RetrieveAPIView):
    """GET /api/contracts/{id}"""
    serializer_class = ContractSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        user = self.request.user
        if user.role == User.Role.CONTRACTOR:
            return Contract.objects.filter(contractor=user)
        return Contract.objects.filter(company=user.company)