# Generated by Django 5.1.3 on 2025-01-04 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("optics", "0013_delete_appointment"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Contact",
        ),
        migrations.DeleteModel(
            name="Feedback",
        ),
        migrations.DeleteModel(
            name="Quote",
        ),
    ]
