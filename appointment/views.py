from django.shortcuts import render

from optics.models import Service


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
    pass