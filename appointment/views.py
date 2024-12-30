import datetime

from django.shortcuts import render
from django.utils import timezone

from appointment.forms import SecondStepForm
from optics.models import Service
from users.models import User


# Create your views here.

def step_1(request):
    service_pk = request.GET.get('service_pk')
    service = Service.objects.filter(pk=service_pk).first()
    object_list = service.medic.all()

    context = {
        'service_pk' : service_pk,
        'object_list' : object_list,
    }

    return render (request, 'appointment/step_1.html', context)

def step_2(request):
    if request.method == 'GET':
        service_pk = request.GET.get('service_pk')
        medic_pk = request.GET.get('medic_pk')
        appointment_day = timezone.now().date()
        form = SecondStepForm(initial={
            'service_pk' : service_pk,
            'medic_pk' : medic_pk,
            'appointment_day' : appointment_day.isoformat(),
        })

        service = Service.objects.filter(pk=service_pk).first()
        medic = User.objects.filter(pk=medic_pk).first()

        context = {
            'form' : form,
            'service' : service,
            'medic' : medic,
        }

        return render (request, 'appointment/step_2.html', context)

def step_3(request):
    return render(request, 'appointment/step_3.html', )
