from django.db import models

from config.settings import NULLABLE
from optics.models import Service
from users.models import User


class Appointment(models.Model):
    day = models.DateField()
    time = models.TimeField()
    comment = models.CharField(max_length=100, **NULLABLE)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE, **NULLABLE,
                                 related_name='appointments', verbose_name='Владелец')
    service = models.ForeignKey(to=Service, on_delete=models.PROTECT,
                                 related_name='appointments', verbose_name='Услуга')
