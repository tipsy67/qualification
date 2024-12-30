import datetime

from django import forms
from django.utils import timezone


class SecondStepForm(forms.Form):
    service_pk = forms.IntegerField(widget=forms.HiddenInput())
    staff_pk = forms.IntegerField(widget=forms.HiddenInput())
    appointment_day = forms.DateField(
        label='Выберите дату',
        widget=forms.DateInput(attrs={'type': 'date',
                                      'min': timezone.now().date().isoformat(),
                                      'max': (timezone.now().date()+datetime.timedelta(30)).isoformat()})
    )

class ThirdStepForm(forms.Form):
    service_pk = forms.IntegerField(widget=forms.HiddenInput())
    staff_pk = forms.IntegerField(widget=forms.HiddenInput())
    appointment_day = forms.DateField(widget=forms.HiddenInput())

# class FoursStepForm(forms.Form):
#     service_pk = forms.IntegerField(widget=forms.HiddenInput())
#     staff_pk = forms.IntegerField(widget=forms.HiddenInput())
#     appointment_day = forms.DateField(widget=forms.HiddenInput())
#     appointment_slot = forms.CharField()
