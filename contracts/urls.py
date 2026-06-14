from django.urls import path
from .views import ContractTemplateListCreateView, ContractListCreateView, ContractDetailView, ContractSignView

urlpatterns = [
    path('contracts/templates/', ContractTemplateListCreateView.as_view(), name='contract-templates'),
    path('contracts/', ContractListCreateView.as_view(), name='contracts'),
    path('contracts/<int:id>/', ContractDetailView.as_view(), name='contract-detail'),
    path('contracts/<int:id>/sign/', ContractSignView.as_view(), name='contract-sign'),
]