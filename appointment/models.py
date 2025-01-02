from django.db import models

from config.settings import NULLABLE, DEFAULT_BEGIN_TIME, DEFAULT_END_TIME
from optics.models import Service
from users.models import User


class Appointment(models.Model):
    day = models.DateField(verbose_name='День')
    time = models.TimeField(verbose_name='Время')
    comment = models.CharField(max_length=100, **NULLABLE,verbose_name='Комментарий')
    owner = models.ForeignKey(to=User, on_delete=models.SET_NULL, **NULLABLE,
                                 related_name='appointments', verbose_name='Владелец')
    service = models.ForeignKey(to=Service, on_delete=models.SET_NULL, **NULLABLE,
                                 related_name='appointments', verbose_name='Услуга')
    medic = models.ForeignKey(to=User, on_delete=models.SET_NULL, **NULLABLE,
                                 verbose_name='Медик')

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
        ordering = ['service', 'day', 'time']

class Schedule(models.Model):
    day = models.DateField(verbose_name='День')
    begin_time = models.TimeField(default=DEFAULT_BEGIN_TIME, verbose_name='Начало приема')
    end_time = models.TimeField(default=DEFAULT_END_TIME, verbose_name='Конец приема')
    is_working_day = models.BooleanField(default=True, verbose_name='Рабочий день')
    medic = models.ForeignKey(to='users.User', on_delete=models.CASCADE, related_name='shedules', verbose_name='Медик')

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписание'
        ordering = ['medic','day']