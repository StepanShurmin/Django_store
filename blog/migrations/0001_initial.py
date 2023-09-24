# Generated by Django 4.2.5 on 2023-09-23 17:39

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
                ('header', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('slug', models.CharField(blank=True, max_length=100, null=True, verbose_name='slug')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Содержимое')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='blog/', verbose_name='Изображение')),
                ('create_date', models.DateField(blank=True, max_length=50, null=True, verbose_name='Дата создания')),
                ('is_public', models.BooleanField(default=True, verbose_name='Признак публикаций')),
                ('count_views', models.IntegerField(default=0, verbose_name='Количество просмотров')),
            ],
            options={
                'verbose_name': 'Блог',
                'verbose_name_plural': 'Блоги',
            },
        ),
    ]
