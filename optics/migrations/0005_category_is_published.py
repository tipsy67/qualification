# Generated by Django 5.1.3 on 2024-12-14 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('optics', '0004_brand_feedback_is_published_alter_feedback_phone_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='is_published',
            field=models.BooleanField(default=False, verbose_name='Активно'),
        ),
    ]
