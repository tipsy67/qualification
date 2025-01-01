from django.utils import timezone

from appointment.forms import SecondStepForm
from optics.models import Service
from users.models import User

def get_context_data(request):
    """Получение контекста для отображения форм шагов записи на прием"""

    service_pk = request.GET.get('service_pk')
    medic_pk = request.GET.get('medic_pk')
    appointment_day = timezone.now().date()
    form = SecondStepForm(initial={
        'service_pk': service_pk,
        'medic_pk': medic_pk,
        'appointment_day': appointment_day.isoformat(),
    })

    service = Service.objects.filter(pk=service_pk).first()
    medic = User.objects.filter(pk=medic_pk).first()

    return {'form': form, 'service': service, 'medic': medic}

def str_list_to_int(list_):
    return [int(x) for x in list_]

def create_time_slots():
    duration = 30
    time = '10:00'
    time_list = str_list_to_int(time.split(':'))
    end_time = '16:00'
    end_time_list = str_list_to_int(end_time.split(':'))
    time_slots = []
    while time_list[0] < end_time_list[0]:
        time_slots.append(str(time_list[0]) + ':' + str(time_list[1]))
        time_list[1] = time_list[1] + duration
        if time_list[1] >=60:
            time_list[0] = time_list[0] + time_list[1]//60
            time_list[1] = time_list[1]%60

    return time_slots

def get_time_slots():
    return create_time_slots()