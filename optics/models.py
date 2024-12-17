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
    image = models.ImageField(upload_to='products/', **NULLABLE, verbose_name='Изображение')
    is_published = models.BooleanField(default=False, verbose_name='Публиковать')

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
        ordering = ['name']

    def __str__(self):
        return f"{self.name}"


class ResultOfService(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(blank=True, verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Изменен')
    service = models.ForeignKey(to=Service, on_delete=models.PROTECT,
                                 related_name='results', verbose_name='Услуга')
    owner = models.ForeignKey(to=User, on_delete=models.SET_NULL, **NULLABLE,
                                 related_name='results', verbose_name='Владелец')

    class Meta:
        verbose_name = 'Результат услуги'
        verbose_name_plural = 'Результаты услуг'
        ordering = ['name']

    def __str__(self):
        return f"{self.name}"


class Feedback(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя')
    phone = models.CharField(max_length=20, verbose_name='Телефон', **NULLABLE)
    message = models.TextField(blank=True, verbose_name='Сообщение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    is_read = models.BooleanField(default=False, verbose_name='Прочитано')
    is_published = models.BooleanField(default=False, verbose_name='Публиковать')

    def __str__(self):
        return f"{self.name}, {self.created_at}"

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

class Quote(models.Model):
    name = models.CharField(max_length=150, verbose_name='Имя')
    quote = models.TextField(blank=True, verbose_name='Сообщение')
    is_published = models.BooleanField(default=False, verbose_name='Публиковать')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Цитата'
        verbose_name_plural = 'Цитаты'

class Contact(models.Model):
    country = models.CharField(max_length=50, verbose_name='Страна')
    inn = models.CharField(max_length=20, verbose_name='ИНН')
    address = models.CharField(max_length=255, verbose_name='Адрес')
    phone = models.CharField(max_length=30, verbose_name='Телефон')
    email = models.EmailField(verbose_name='Эл.почта')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.email}"

    class Meta:
        ordering = ['-updated_at']
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'