# Generated by Django 5.1.3 on 2024-12-24 20:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('optics', '0013_delete_appointment'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('day', models.DateField()),
                ('time', models.TimeField()),
                ('comment', models.CharField(blank=True, max_length=100, null=True)),
                (
                    'owner',
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='appointments',
                        to=settings.AUTH_USER_MODEL,
                        verbose_name='Владелец',
                    ),
                ),
                (
                    'service',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name='appointments',
                        to='optics.service',
                        verbose_name='Услуга',
                    ),
                ),
            ],
        ),
    ]
