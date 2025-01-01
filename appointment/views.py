from django.shortcuts import render, redirect
from django.utils import timezone

from appointment.forms import SecondStepForm, ThirdStepForm
from appointment.src.utils import get_time_slots
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
    service_pk = request.GET.get('service_pk')
    medic_pk = request.GET.get('medic_pk')
    appointment_day = request.GET.get('date')
    if appointment_day is None:
        appointment_day = timezone.now().date().isoformat()
    form = SecondStepForm(initial={
        'service_pk': service_pk,
        'medic_pk': medic_pk,
        'appointment_day': appointment_day,
    })

    service = Service.objects.filter(pk=service_pk).first()
    medic = User.objects.filter(pk=medic_pk).first()

    context = {'form': form, 'service': service, 'medic': medic}

    return render (request, 'appointment/step_2.html', context)


def step_3(request):
    if request.method == 'POST':
        form = SecondStepForm(request.POST)
        if form.is_valid():
            service = Service.objects.filter(pk=form.data.get('service_pk')).first()
            medic = User.objects.filter(pk=form.data.get('medic_pk')).first()

            next_form = ThirdStepForm(initial=form.data)
            next_form.fields['appointment_slot'].choices = get_time_slots()

            context = {'form': next_form, 'service': service, 'medic': medic, 'date': form.data.get('appointment_day')}
            return render(request, 'appointment/step_3.html', context)
        else:

            return redirect(request, 'appointment/step_2.html', form.data)

def step_4(request):
    if request.method == 'POST':
        form = SecondStepForm(request.POST)
        if form.is_valid():
            service = Service.objects.filter(pk=form.data.get('service_pk')).first()
            medic = User.objects.filter(pk=form.data.get('medic_pk')).first()

            context = {'service': service, 'medic': medic,
                       'date': form.data.get('appointment_day'), 'slot': form.data.get('appointment_slot')}
            return render(request, 'appointment/thank-you.html', context)
        else:

            return redirect(request, 'appointment/step_3.html', form.data)