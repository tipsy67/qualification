# Generated by Django 5.1.3 on 2024-12-13 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('slug', models.CharField(max_length=100, unique=True, verbose_name='Slug')),
                ('image', models.ImageField(blank=True, upload_to='products/', verbose_name='Изображение')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Изменен')),
                ('is_published', models.BooleanField(default=False, verbose_name='Признак публикации')),
                ('views_counter', models.IntegerField(default=0, verbose_name='Количество просмотров')),
                ('content', models.TextField(verbose_name='Содержимое')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
                'ordering': ['-created_at'],
                'permissions': [('can_publish_article', 'Can publish article')],
            },
        ),
    ]
