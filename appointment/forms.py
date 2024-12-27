from django import forms


class SecondStepForm(forms.Form):
    service_pk = forms.IntegerField(widget=forms.HiddenInput())
    staff_pk = forms.IntegerField(widget=forms.HiddenInput())
    appointment_day = forms.DateField(widget=forms.HiddenInput())

class ThirdStepForm(forms.Form):
    service_pk = forms.IntegerField(widget=forms.HiddenInput())
    staff_pk = forms.IntegerField(widget=forms.HiddenInput())
    appointment_day = forms.DateField(widget=forms.HiddenInput())

# class FoursStepForm(forms.Form):
#     service_pk = forms.IntegerField(widget=forms.HiddenInput())
#     staff_pk = forms.IntegerField(widget=forms.HiddenInput())
#     appointment_day = forms.DateField(widget=forms.HiddenInput())
#     appointment_slot = forms.CharField()
