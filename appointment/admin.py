from django.contrib import admin

from appointment.models import Appointment


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    pass
