from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    photo = models.ImageField(upload_to="users/%Y/%m/%d/", blank=True, null=True, verbose_name="Фотография")
    number = models.PositiveBigIntegerField(blank=True, null=True, verbose_name='Контактный телефон')
    address = models.CharField(max_length=100, blank=True, null=True, verbose_name='Адрес')