# Generated by Django 5.1.3 on 2024-12-25 19:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_image_user_is_a_medic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_a_medic',
            new_name='is_medic',
        ),
    ]
