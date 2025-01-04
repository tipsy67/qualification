from django.contrib import admin

from appointment.models import Appointment, Schedule, ResultOfService, Eye
from users.models import User


class MedicFilter(admin.SimpleListFilter):
    title = 'Сотрудник'
    parameter_name = 'medic'

    def lookups(self, request, model_admin):
        users = User.objects.filter(is_medic=True)
        return [(user.id, f"{user.last_name} {user.first_name[:1]}.") for user in users]

    def queryset(self, request, queryset):
        if self.value() is None:
            return queryset.all()
        return queryset.filter(medic=self.value())

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('service', 'day', 'time', 'owner', 'medic', 'comment')
    list_filter = ('service', 'day', 'time', 'owner', MedicFilter)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "medic":
            kwargs["queryset"] = User.objects.filter(is_medic=True)
        return super(AppointmentAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('medic', 'day', 'is_working_day', 'begin_time', 'end_time')
    list_filter = (MedicFilter, 'day')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "medic":
            kwargs["queryset"] = User.objects.filter(is_medic=True)
        return super(ScheduleAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(ResultOfService)
class ResultOfServiceAdmin(admin.ModelAdmin):
    pass

@admin.register(Eye)
class EyeAdmin(admin.ModelAdmin):
    pass

