from django.urls import path

from appointment.apps import AppointmentConfig
from appointment.views import step_1, step_2

appname = AppointmentConfig.name

urlpatterns = [
   path ('appointment/step-1/', step_1, name='step-1'),
   path ('appointment/step-2/', step_2, name='step-2'),
]