# Generated by Django 5.1.3 on 2024-12-15 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('optics', '0005_category_is_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='active_on_main_page',
            field=models.BooleanField(default=False, verbose_name='Активно на гл.стр.'),
        ),
    ]
