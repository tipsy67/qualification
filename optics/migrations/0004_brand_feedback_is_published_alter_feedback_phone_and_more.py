# Generated by Django 5.1.3 on 2024-12-14 19:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('optics', '0003_product_parameter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
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
                ('name', models.CharField(max_length=100, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Бренд',
                'verbose_name_plural': 'Бренды',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='feedback',
            name='is_published',
            field=models.BooleanField(default=False, verbose_name='Публиковать'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='phone',
            field=models.CharField(
                blank=True, max_length=20, null=True, verbose_name='Телефон'
            ),
        ),
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name='products',
                to='optics.brand',
                verbose_name='Бренд',
            ),
        ),
    ]
