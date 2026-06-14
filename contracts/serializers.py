from rest_framework import serializers
from .models import ContractTemplate, Contract


class ContractTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractTemplate
        fields = ['id', 'name', 'body_template', 'created_at']
        read_only_fields = ['id', 'created_at']


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = [
            'id', 'company', 'template', 'contractor',
            'contract_number', 'subject', 'amount', 'status',
            'signed_at', 'file_url', 'created_at'
        ]
        read_only_fields = ['id', 'company', 'contract_number', 'status', 'signed_at','file_url', 'created_at']

class ContractCreateSerializer(serializers.Serializer):
    """Contract create"""
    template_id = serializers.IntegerField(required=False)
    contractor_id = serializers.IntegerField()
    subject = serializers.CharField()
    amount = serializers.DecimalField(max_digits=12, decimal_places=2)