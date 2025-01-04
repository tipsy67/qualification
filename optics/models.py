from django.db import models

from config.settings import NULLABLE
from users.models import User


class Brand(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    ordering = ['name']

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'
        ordering = ['name']

    def __str__(self):
        return f"{self.name}"

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(blank=True, verbose_name='Описание')
    is_published = models.BooleanField(default=False, verbose_name='Активно')
    active_on_main_page = models.BooleanField(default=False, verbose_name='Активно на гл.стр.')

    ordering = ['name']

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    brand = models.ForeignKey(to=Brand, on_delete=models.PROTECT,
                                 related_name='products', verbose_name='Бренд', **NULLABLE)
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    price = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Цена')
    image = models.ImageField(upload_to='products/', **NULLABLE, verbose_name='Изображение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Изменен')
    category = models.ForeignKey(to=Category, on_delete=models.PROTECT,
                                 related_name='products', verbose_name='Категория')
    owner = models.ForeignKey(to=User, on_delete=models.SET_NULL, **NULLABLE,
                                 related_name='products', verbose_name='Владелец')
    parameter = models.CharField(max_length=30, verbose_name='Параметр', **NULLABLE)
    is_published = models.BooleanField(default=False, verbose_name='Активно')
    # manufactured_at = models.DateField(default=datetime.datetime(2024,4,21))

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name']

    def __str__(self):
        return f"{self.name}"


class Service(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Цена')
    duration = models.PositiveSmallIntegerField(**NULLABLE, verbose_name='Длительность')
    image = models.ImageField(upload_to='products/', **NULLABLE, verbose_name='Изображение')
    is_published = models.BooleanField(default=False, verbose_name='Публиковать')
    medic = models.ManyToManyField("users.User", related_name="services")

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
        ordering = ['name']

    def __str__(self):
        return f"{self.name}"



