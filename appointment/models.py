from django.db import models

from config.settings import DEFAULT_BEGIN_TIME, DEFAULT_END_TIME, NULLABLE
from optics.models import Service
from users.models import User

weekdays = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']

class Eye(models.Model):
    sph = models.DecimalField(
        **NULLABLE, max_digits=5, decimal_places=2, verbose_name='SPH'
    )
    cyl = models.DecimalField(
        **NULLABLE, max_digits=5, decimal_places=2, verbose_name='CYL'
    )
    ax = models.DecimalField(
        **NULLABLE, max_digits=5, decimal_places=2, verbose_name='AX'
    )
    pr = models.DecimalField(
        **NULLABLE, max_digits=5, decimal_places=2, verbose_name='Pr'
    )
    bas = models.DecimalField(
        **NULLABLE, max_digits=5, decimal_places=2, verbose_name='BAS'
    )
    dp = models.DecimalField(
        **NULLABLE, max_digits=5, decimal_places=2, verbose_name='DP'
    )
    add = models.DecimalField(
        **NULLABLE, max_digits=5, decimal_places=2, verbose_name='ADD'
    )

    class Meta:
        verbose_name = 'Результат измерений'
        verbose_name_plural = 'Результаты измерений'

    def __str__(self):
        return f"sph {self.sph} .."


class ResultOfService(models.Model):
    od = models.OneToOneField(
        to=Eye,
        **NULLABLE,
        on_delete=models.CASCADE,
        verbose_name='OD',
        related_name='od',
    )
    os = models.OneToOneField(
        to=Eye,
        **NULLABLE,
        on_delete=models.CASCADE,
        verbose_name='OS',
        related_name='os',
    )
    recommendations = models.TextField(blank=True, verbose_name='Рекомендации')
    comment = models.TextField(blank=True, verbose_name='Комментарий')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Изменен')

    class Meta:
        verbose_name = 'Результат услуги'
        verbose_name_plural = 'Результаты услуг'
        ordering = ['-created_at']

    def __str__(self):
        return f"OD: {self.od}, OS: {self.os}"


class Appointment(models.Model):
    day = models.DateField(verbose_name='День')
    time = models.TimeField(verbose_name='Время')
    comment = models.CharField(max_length=100, **NULLABLE, verbose_name='Комментарий')
    owner = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        **NULLABLE,
        related_name='appointments',
        verbose_name='Владелец',
    )
    service = models.ForeignKey(
        to=Service,
        on_delete=models.SET_NULL,
        **NULLABLE,
        related_name='appointments',
        verbose_name='Услуга',
    )
    medic = models.ForeignKey(
        to=User, on_delete=models.SET_NULL, **NULLABLE, verbose_name='Медик'
    )
    result = models.OneToOneField(
        to=ResultOfService,
        **NULLABLE,
        on_delete=models.CASCADE,
        related_name='appointment',
        verbose_name='Результат',
    )

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
        ordering = ['service', 'day', 'time']

    def __str__(self):
        return f"{self.owner} {self.service} ({self.day})"


class Schedule(models.Model):
    day = models.DateField(verbose_name='День')
    begin_time = models.TimeField(
        default=DEFAULT_BEGIN_TIME, verbose_name='Начало приема'
    )
    end_time = models.TimeField(default=DEFAULT_END_TIME, verbose_name='Конец приема')
    is_working_day = models.BooleanField(default=True, verbose_name='Рабочий день')
    medic = models.ForeignKey(
        to='users.User',
        on_delete=models.CASCADE,
        related_name='shedules',
        verbose_name='Медик',
    )

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписание'
        ordering = ['medic', 'day']

    def __str__(self):
        return f"{self.medic} {self.day} {self.begin_time} {self.end_time}"

    @property
    def day_of_week(self):
        return weekdays[self.day.weekday()]
