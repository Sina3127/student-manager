from django import forms
from django.forms import inlineformset_factory

from college.models import Agreement, Duration


class AgreementForm(forms.ModelForm):
    class Meta:
        model = Agreement
        fields = ('students_name', 'number_of_classes', 'price')


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
