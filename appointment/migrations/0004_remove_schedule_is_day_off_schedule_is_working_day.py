# Generated by Django 5.1.3 on 2025-01-02 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("appointment", "0003_appointment_medic_alter_appointment_owner_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="schedule",
            name="is_day_off",
        ),
        migrations.AddField(
            model_name="schedule",
            name="is_working_day",
            field=models.BooleanField(default=True, verbose_name="Выходной"),
        ),
    ]
