from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    product_name = models.CharField(max_length=50, verbose_name='наименование')
    product_description = models.CharField(max_length=200, verbose_name='описание продукта', **NULLABLE)
    product_image = models.ImageField(upload_to='products/', verbose_name='изображение', **NULLABLE)
    product_category = models.CharField(max_length=50, verbose_name='категория')
    product_price = models.FloatField(verbose_name='цена')
    product_date_creation = models.DateField(verbose_name='дата создания', **NULLABLE)
    product_date_modification = models.DateField(verbose_name='дата последнего изменения', **NULLABLE)

    is_active = models.BooleanField(default=True, verbose_name='в наличии')

    def __str__(self):
        return f'{self.product_name} {self.product_category} {self.product_price} {self.product_date_creation}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('product_category', 'product_name', 'product_date_modification')


class Category(models.Model):
    category_name = models.CharField(max_length=50, verbose_name='наименование')
    category_description = models.CharField(max_length=200, verbose_name='описание')

    is_active = models.BooleanField(default=True, verbose_name='в наличии')

    def __str__(self):
        return f'{self.category_name} {self.category_description}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('category_name',)
