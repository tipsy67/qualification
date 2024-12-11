from django.db import models

class Product(models.Model):
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
    is_published = models.BooleanField(default=False, verbose_name='Активно')
    # manufactured_at = models.DateField(default=datetime.datetime(2024,4,21))

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name']
        permissions = [
            ('can_edit_description', 'может редактировать описание'),
            ('can_edit_category', 'может редактировать категорию'),
            ('can_published', 'может публиковать продукт'),
        ]

    def __str__(self):
        return f"{self.name}"

class Category(models.Model):
    pass

class Service(models.Model):
    pass

class Result_of_Service:
    pass

class Feedback(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    message = models.TextField(blank=True, verbose_name='Сообщение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    is_read = models.BooleanField(default=False, verbose_name='Прочитано')

    def __str__(self):
        return f"{self.name}, {self.created_at}"

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
