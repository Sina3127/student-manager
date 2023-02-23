from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic

from college.models import Contract


class ContractsView(LoginRequiredMixin, generic.ListView):
    template_name = 'college/contracts.html'
    model = Contract
    paginate_by = 10
    order_by = 'id'
    allow_empty = False
    context_object_name = 'contract_list'

class ContractDetailsView(LoginRequiredMixin, generic.DetailView):
    template_name = 'college/contracts_details.html'
    model = Contract
    context_object_name = 'contract'
    pk_url_kwarg = 'id'
