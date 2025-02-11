from django.urls import path

from appointment.apps import AppointmentConfig
from appointment.views import (
    appointments_detail,
    appointments_list,
    step_1,
    step_2,
    step_3,
    step_4,
)

appname = AppointmentConfig.name

urlpatterns = [
    path('appointment/step-1/', step_1, name='step-1'),
    path('appointment/step-2/', step_2, name='step-2'),
    path('appointment/step-3/', step_3, name='step-3'),
    path('appointment/step-4/', step_4, name='step-4'),
    path('appointment-list/', appointments_list, name='appointment-list'),
    path(
        'appointment-detail/<int:pk>/', appointments_detail, name='appointment-detail'
    ),
]
