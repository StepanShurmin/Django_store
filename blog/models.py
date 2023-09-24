from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.CharField(max_length=100, **NULLABLE, verbose_name='slug')
    body = models.TextField(**NULLABLE, verbose_name='Содержимое')
    image = models.ImageField(upload_to='blog/', **NULLABLE, verbose_name='Изображение')
    create_date = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    is_published = models.BooleanField(default=True, verbose_name='Признак публикаций')
    count_views = models.IntegerField(default=0, verbose_name='Количество просмотров')

    def __str__(self):
        return f"{self.title} {self.slug} {self.body} {self.count_views}"

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
