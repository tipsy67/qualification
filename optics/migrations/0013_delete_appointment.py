# Generated by Django 5.1.3 on 2024-12-24 20:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('optics', '0012_service_duration_appointment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Appointment',
        ),
    ]
