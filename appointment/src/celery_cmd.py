from datetime import datetime, timedelta
from appointment.tasks import sendmail

from appointment.models import Appointment
from users.models import User


def write_reminder(owner_pk: int, appointment_pk: int):
    appointment = Appointment.objects.filter(pk=appointment_pk).first()
    owner = User.objects.filter(pk=owner_pk).first()

    eta = datetime.combine(appointment.day - timedelta(days=1), appointment.time)

    sendmail.apply_async(
        args=[
            [owner.email],
            "Запись на прием",
            f"Добрый день, {owner.first_name}!\n"
            f"Напоминаем вам, что {appointment.day}\n"
            f"в {appointment.time} у Вас запись на прием.\n"
            f"Врач {appointment.medic.last_name} {appointment.medic.first_name}\n"
            f"на услугу: '{appointment.service}' \n",
        ],
        eta=eta,
        task_id = f"appointment_task_{appointment_pk}"
    )


