from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class User(AbstractUser):
    photo = models.ImageField(upload_to="users/%Y/%m/%d/", blank=True, null=True, verbose_name="Фотография")
    number = models.PositiveBigIntegerField(blank=True, null=True, verbose_name='Контактный телефон')
    address = models.CharField(max_length=100, blank=True, null=True, verbose_name='Адрес')
    email = models.EmailField(unique=True, verbose_name='Email')

    def get_absolute_url(self):
        return reverse('users:profile_user', kwargs={'user_id': self.id})