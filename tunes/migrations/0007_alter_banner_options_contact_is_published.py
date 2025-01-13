# Generated by Django 5.1.3 on 2025-01-09 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tunes", "0006_banner_alter_quote_quote"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="banner",
            options={
                "ordering": ["title"],
                "verbose_name": "Заглавный баннер",
                "verbose_name_plural": "Заглавные баннеры",
            },
        ),
        migrations.AddField(
            model_name="contact",
            name="is_published",
            field=models.BooleanField(default=False, verbose_name="Активно"),
        ),
    ]
