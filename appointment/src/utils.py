from appointment.models import Schedule, Appointment
from config.settings import DEFAULT_SERVICE_DURATION, DEFAULT_BEGIN_TIME, DEFAULT_END_TIME
from optics.models import Service
from users.models import User


def str_list_to_int(list_) -> list:
    return [int(x) for x in list_]


def create_time_slots(day, service: Service , medic:User):
    duration = service.duration
    if duration is None:
        duration = DEFAULT_SERVICE_DURATION

    shedule = Schedule.objects.filter(day=day, medic=medic).first()

    if shedule is None:
        time = DEFAULT_BEGIN_TIME
        end_time = DEFAULT_END_TIME
    else:
        if not shedule.is_working_day:
            return []
        time = shedule.begin_time.strftime('%H:%M')
        end_time = shedule.end_time.strftime('%H:%M')


    time_list = str_list_to_int(time.split(':'))
    end_time_list = str_list_to_int(end_time.split(':'))
    time_slots = []
    while time_list[0] < end_time_list[0]:
        time = f"{time_list[0]:02}" + ':' + f"{time_list[1]:02}"
        time_slots.append((time,time))
        time_list[1] = time_list[1] + duration
        if time_list[1] >=60:
            time_list[0] = time_list[0] + time_list[1]//60
            time_list[1] = time_list[1]%60

    return time_slots

def get_busy_time_slots(day, medic: User):
    appointment_list = Appointment.objects.filter(day=day, medic=medic)

    return [(x.time.strftime('%H:%M')) for x in appointment_list]

def get_time_slots(day, service: Service, medic: User):
    time_slots = create_time_slots(day, service, medic)
    busy_time_slots = get_busy_time_slots(day, medic)

    if busy_time_slots:
        time_slots = [x for x in time_slots if x[0] not in busy_time_slots]

    return time_slots

