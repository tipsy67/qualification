import datetime

from django import forms
from django.utils import timezone


class SecondStepForm(forms.Form):
    service_pk = forms.IntegerField(widget=forms.HiddenInput())
    medic_pk = forms.IntegerField(widget=forms.HiddenInput())
    appointment_day = forms.DateField(
        label='Выберите дату',
        widget=forms.DateInput(attrs={'type': 'date',
                                      'min': timezone.now().date().isoformat(),
                                      'max': (timezone.now().date()+datetime.timedelta(30)).isoformat()})
    )

class ThirdStepForm(forms.Form):
    service_pk = forms.IntegerField(widget=forms.HiddenInput())
    medic_pk = forms.IntegerField(widget=forms.HiddenInput())
    appointment_day = forms.DateField(
        label='На дату',
        widget=forms.DateInput(attrs={'type': 'date',
                                      'readonly': True}),
    )
    appointment_slot = forms.ChoiceField(label='Выберите время', choices=[])
