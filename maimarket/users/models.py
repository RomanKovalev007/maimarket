from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
import random

class User(AbstractUser):
    photo = models.ImageField(upload_to="users/%Y/%m/%d/", blank=True, null=True, verbose_name="Фотография")
    number = models.PositiveBigIntegerField(blank=True, null=True, verbose_name='Контактный телефон')
    address = models.CharField(max_length=100, blank=True, null=True, verbose_name='Адрес')
    email = models.EmailField(unique=True, verbose_name='Email')
    telegram = models.SlugField(null=True, blank=True, verbose_name='Ссылка на телеграмм')

    def get_absolute_url(self):
        return reverse('users:profile', kwargs={'user_id': self.id})

class EmailVerification(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    email = models.EmailField()
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    @classmethod
    def generate_code(cls):
        return str(random.randint(100000, 999999))