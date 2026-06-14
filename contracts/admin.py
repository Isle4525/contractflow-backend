from django.contrib import admin

from contracts.models import ContractTemplate, Contract


@admin.register(ContractTemplate)
class ContractTemplateAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'company')

@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('id', 'contract_number', 'company', 'contractor', 'amount', 'status')
    list_filter = ('status', 'company')
