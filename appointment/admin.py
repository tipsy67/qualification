from datetime import timedelta, time

from django.contrib import admin

from appointment.models import Appointment, Eye, ResultOfService, Schedule
from appointment.src.celery_cmd import write_reminder
from tunes.models import TunesDict
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
        return super(AppointmentAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs
        )

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        write_reminder(obj.owner.pk, obj.pk)

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):

    list_display = ('medic', 'day', 'ru_day_of_week', 'is_working_day', 'begin_time', 'end_time')
    list_filter = (MedicFilter, 'day')
    actions = ('set_day_off', 'set_day_working', 'create_7_days_schedule', 'create_30_days_schedule')
    readonly_fields = ('ru_day_of_week',)

    @admin.display(description='День недели')
    def ru_day_of_week(self, obj):
        return obj.day_of_week

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "medic":
            kwargs["queryset"] = User.objects.filter(is_medic=True)
        return super(ScheduleAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs
        )

    @admin.action(description="Сделать выходным днем")
    def set_day_off(self, request, queryset):
        count = queryset.update(is_working_day=False)
        self.message_user(request, f"Изменено {count} записи(ей).")

    @admin.action(description="Сделать рабочим днем")
    def set_day_working(self, request, queryset):
        count = queryset.update(is_working_day=True)
        self.message_user(request, f"Изменено {count} записи(ей).")


    def create_new_schedule(self, request, queryset, num_of_days:int):
        obj = queryset.order_by('-day').first()
        if obj is not None:
            begin_time = TunesDict.objects.filter(key="begin_time").first()
            end_time = TunesDict.objects.filter(key="end_time").first()
            for i in range(1,num_of_days+1):
                flag = False
                new_obj = Schedule.objects.create(day=obj.day + timedelta(days=i), medic=obj.medic)
                if begin_time is not None:
                    flag=True
                    new_obj.begin_time = begin_time.value_time
                if end_time is not None:
                    flag=True
                    new_obj.end_time = end_time.value_time
                if flag:
                    new_obj.save()
            self.message_user(request, f"Добавлено {num_of_days} дней в расписание.")
        else:
            self.message_user(request, f"Ошибка при создании расписания.")


    @admin.action(description="Добавить 7 дней")
    def create_7_days_schedule(self, request, queryset):
        self.create_new_schedule(request, queryset, 7)

    @admin.action(description="Добавить 30 дней")
    def create_30_days_schedule(self, request, queryset):
        self.create_new_schedule(request, queryset, 30)


@admin.register(ResultOfService)
class ResultOfServiceAdmin(admin.ModelAdmin):
    pass

@admin.register(Eye)
class EyeAdmin(admin.ModelAdmin):
    pass
