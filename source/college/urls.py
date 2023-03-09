from django.urls import path

from college.views import ContractsView, ContractDetailsView, AgreementView, AgreementDetailsView

app_name = 'college'

urlpatterns = [
    path('contracts/', ContractsView.as_view(), name='contracts'),
    path('contracts/<int:id>/', ContractDetailsView.as_view(), name='contract_details'),
    path('contracts/<int:id>/create/', AgreementView.as_view(), name='agreement_create'),
    path('agreement/<int:id>/', AgreementDetailsView.as_view(), name='agreement_details'),
]