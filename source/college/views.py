from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from college.forms import AgreementForm, DurationFormSet
from college.models import Contract, Agreement


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


class AgreementView(LoginRequiredMixin, generic.CreateView):
    form_class = AgreementForm
    model = Agreement
    template_name = 'college/agreement_create.html'

    def get_context_data(self, **kwargs):
        ctx = super(AgreementView, self).get_context_data(**kwargs)
        if self.request.method == 'GET':
            ctx['named_formsets'] = DurationFormSet(prefix='duration')
        else:
            ctx['named_formsets'] = DurationFormSet(self.request.POST or None, self.request.FILES or None, prefix='duration')
        return ctx

    def form_valid(self, form):
        pass
