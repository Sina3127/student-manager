from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect
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
        ctx['named_formsets'] = self.get_named_formsets()
        return ctx

    def get_named_formsets(self):
        if self.request.method == 'GET':
            return {
                'variants': DurationFormSet(prefix='duration')
            }
        else:
            return {
                'variants': DurationFormSet(self.request.POST or None, self.request.FILES or None,
                                            prefix='duration')
            }

    def get(self, request, *args, **kwargs):
        self.contract = get_object_or_404(Contract, pk=kwargs['id'])
        return super(AgreementView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.contract = get_object_or_404(Contract, pk=kwargs['id'])
        return super(AgreementView, self).post(request, *args, **kwargs)

    def form_valid(self, form):
        named_formsets = self.get_named_formsets()
        if not all((x.is_valid() for x in named_formsets.values())):
            return self.render_to_response(self.get_context_data(form=form))
        agreement = form.save()
        formset = named_formsets['variants']
        variants = formset.save(commit=False)
        for Duration in variants:
            Duration.agreement = agreement
            Duration.save()

        return redirect('college:agreement_details', id=agreement.id)

    def get_form_kwargs(self):
        kwargs = super(AgreementView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        kwargs['contract'] = self.contract
        return kwargs


class AgreementDetailsView(LoginRequiredMixin, generic.DetailView):
    template_name = 'college/agreement_details.html'
    model = Agreement
    context_object_name = 'agreement'
    pk_url_kwarg = 'id'

    def get_object(self, queryset=None):
        instance = super(AgreementDetailsView, self).get_object(queryset)
        if instance.user != self.request.user:
            raise PermissionDenied("you can't access this agreement")
        return instance


class AgreementListView(LoginRequiredMixin, generic.ListView):
    template_name = 'college/agreement_list.html'
    paginate_by = 10
    order_by = 'id'
    allow_empty = False
    context_object_name = 'agreement_list'

    def get_queryset(self):
        return Agreement.objects.filter(user=self.request.user).all()
