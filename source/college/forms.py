from django import forms
from django.forms import inlineformset_factory

from college.models import Agreement, Duration


class AgreementForm(forms.ModelForm):
    class Meta:
        model = Agreement
        fields = ('students_name', 'number_of_classes', 'price')

    def __init__(self, user, contract, *args, **kwargs):
        super(AgreementForm, self).__init__(*args, **kwargs)
        self.user = user
        self.contract = contract

    def save(self, commit=True):
        self.instance.user = self.user
        self.instance.contract = self.contract
        super(AgreementForm, self).save(commit)


class DurationForm(forms.ModelForm):
    class Meta:
        model = Duration
        fields = ('start_date', 'end_date', 'agreement')
        widgets = {
            'start_date': forms.DateInput(format='%d/%m/%Y',
                                          attrs={'class': 'form-control',
                                                 'placeholder': 'Select a date',
                                                 'type': 'date'
                                                 }),
            'end_date': forms.DateInput(format='%d/%m/%Y',
                                        attrs={'class': 'form-control',
                                               'placeholder': 'Select a date',
                                               'type': 'date'
                                               }),
        }


DurationFormSet = inlineformset_factory(
    Agreement, Duration, form=DurationForm,
    extra=1, min_num=1, can_delete=False,
)
