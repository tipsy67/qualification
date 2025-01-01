import copy
import datetime

from django.shortcuts import render
from django.utils import timezone

from appointment.forms import SecondStepForm, ThirdStepForm
from appointment.src.utils import get_context_data
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
    context = get_context_data(request)
    if request.method == 'GET':
         return render (request, 'appointment/step_2.html', context)
    else:
        form = SecondStepForm(request.POST)
        if form.is_valid():
            next_form = ThirdStepForm(initial=form.data)
            context['form'] = next_form
            return render(request, 'appointment/step_3.html', context)
        else:
            context['form'] = form
            return render(request, 'appointment/step_2.html', context)


def step_3(request,context):
    if request.method == 'GET':
        return render(request, 'appointment/step_3.html', context)
    else:
        return render(request, 'appointment/thank-you.html', context)
