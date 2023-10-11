from django.contrib.auth.models import AbstractUser
from django.db import models

from catalog.models import NULLABLE


class User(AbstractUser):
    """Модель пользователя."""
    username = None

    email = models.EmailField(unique=True, verbose_name='Почта')

    avatar = models.ImageField(upload_to='users/', verbose_name='Аватар', **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name='Номер телефона', **NULLABLE)
    country = models.CharField(max_length=30, verbose_name='Страна', **NULLABLE)
    email_verified = models.BooleanField(default=False)
    verification_token = models.CharField(max_length=255, **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
