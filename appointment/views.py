from django.shortcuts import render, redirect
from django.utils import timezone

from appointment.forms import SecondStepForm, ThirdStepForm
from appointment.models import Appointment, ResultOfService
from appointment.src.utils import get_time_slots
from config.settings import MAIN_STREAMER_PATH
from optics.models import Service
from users.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def step_1(request):
    service_pk = request.GET.get('service_pk')
    service = Service.objects.filter(pk=service_pk).first()
    object_list = service.medic.all()

    context = {
        'service_pk' : service_pk,
        'object_list' : object_list,
    }

    return render (request, 'appointment/step_1.html', context)

@login_required
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

@login_required
def step_3(request):
    if request.method == 'POST':
        form = SecondStepForm(request.POST)
        if form.is_valid():
            service = Service.objects.filter(pk=form.data.get('service_pk')).first()
            medic = User.objects.filter(pk=form.data.get('medic_pk')).first()
            day = form.data.get('appointment_day')

            next_form = ThirdStepForm(initial=form.data)
            next_form.fields['appointment_slot'].choices = get_time_slots(day, service, medic)

            context = {'form': next_form, 'service': service, 'medic': medic, 'date': day}
            return render(request, 'appointment/step_3.html', context)
        else:

            return redirect(request, 'appointment/step_2.html', form.data)

@login_required
def step_4(request):
    if request.method == 'POST':
        form = SecondStepForm(request.POST)
        if form.is_valid():
            service = Service.objects.filter(pk=form.data.get('service_pk')).first()
            medic = User.objects.filter(pk=form.data.get('medic_pk')).first()
            day = form.data.get('appointment_day')
            time = form.data.get('appointment_slot')
            owner = request.user

            Appointment.objects.create(day=day, time=time, service=service, owner=owner, medic=medic)

            context = {'service': service, 'medic': medic,
                       'date': day, 'slot': time}
            return render(request, 'appointment/thank-you.html', context)
        else:

            return redirect(request, 'appointment/step_3.html', form.data)

def appointments_list(request):
    object_list = Appointment.objects.filter(owner=request.user)

    streamer_content = {'title' : 'Медкарта'}
    streamer_path = MAIN_STREAMER_PATH.copy()
    streamer_path.append({'name' : 'Записи', 'url' : 'appointment:appointment-list'})
    streamer_content['path'] = streamer_path


    context = {
        'object_list': object_list,
        'streamer_content': streamer_content,
    }

    return render(request, 'appointment/appointment-list.html', context)


def appointments_detail(request, pk):

    streamer_content = {'title' : 'Медкарта'}
    streamer_path = MAIN_STREAMER_PATH.copy()
    streamer_path.append({'name' : 'Записи', 'url' : 'appointment:appointment-list'})
    streamer_path.append({'name' : 'Текущая', })
    streamer_content['path'] = streamer_path

    result = ResultOfService.objects.filter(pk=pk).first()

    context = {
        'streamer_content': streamer_content,
        'result': result,
    }

    return render(request, 'appointment/appointment-detail.html', context)
