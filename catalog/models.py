from django.conf import settings
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    """Модель товара."""
    name = models.CharField(max_length=50, verbose_name='наименование')
    description = models.CharField(max_length=200, verbose_name='описание продукта', **NULLABLE)
    image = models.ImageField(upload_to='products/', verbose_name='изображение', **NULLABLE)
    category = models.CharField(max_length=50, verbose_name='категория')
    price = models.FloatField(verbose_name='цена')
    date_creation = models.DateField(auto_now_add=True, verbose_name='дата создания', **NULLABLE)
    date_modification = models.DateField(auto_now_add=True, verbose_name='дата последнего изменения', **NULLABLE)
    users = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='пользователь'
    )
    is_active = models.BooleanField(default=True, verbose_name='в наличии')

    def __str__(self):
        """Строковое представление модели товара."""
        return f'{self.name} {self.category} {self.price} {self.date_creation}'

    class Meta:
        """Метаданные о модели."""
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('category', 'name', 'date_modification')


class Category(models.Model):
    """Модель категории."""
    name = models.CharField(max_length=50, verbose_name='наименование')
    description = models.CharField(max_length=200, verbose_name='описание')

    is_active = models.BooleanField(default=True, verbose_name='в наличии')

    def __str__(self):
        """Строковое представление модели товара."""
        return f'{self.name} {self.description}'

    class Meta:
        """Метаданные о модели."""
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('name',)


class Version(models.Model):
    """Модель Версий."""
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    version_number = models.IntegerField(verbose_name='Номер версии')
    version_name = models.CharField(max_length=100, verbose_name='Название версии')
    is_active = models.BooleanField(verbose_name='Признак текущей версии', default=False)

    def __str__(self):
        """Строковое представление модели версии."""
        return f'{self.version_name} | {self.version_number}'

    class Meta:
        """Метаданные о модели."""
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
