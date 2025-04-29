from autoslug import AutoSlugField
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from unicodedata import category

from users.models import User

def translit_to_eng(s: str) -> str:
    d = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd',
         'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i', 'к': 'k',
         'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r',
         'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch',
         'ш': 'sh', 'щ': 'shch', 'ь': '', 'ы': 'y', 'ъ': '', 'э': 'r', 'ю': 'yu', 'я': 'ya'}

    return "".join(map(lambda x: d[x] if d.get(x, False) else x, s.lower()))

class Categories(models.Model):
    name = models.CharField(max_length=127, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=127, unique=True, verbose_name='URL')
    class Meta:
        db_table = 'category'
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

class Address(models.Model):
    name = models.CharField(max_length=127, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=127, unique=True, blank=True, null=True, verbose_name='slug')
    address = models.CharField(max_length=127, unique=True, verbose_name='Адрес')
    link_to_map = models.URLField(max_length=127, unique=True, verbose_name='Ссылка на карту')

    def __str__(self):
        return self.name

class Goods(models.Model):
    name = models.CharField(max_length=127, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=127, unique=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(upload_to="goods/%Y/%m/%d/", blank=True, null=True, verbose_name='Изображение')
    price = models.PositiveIntegerField(default=0, verbose_name='Цена')
    category = models.ForeignKey(to=Categories, on_delete=models.PROTECT, verbose_name='Категория')
    #related_name = 'goods'

    seller = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='Продавец')
    condition = models.BooleanField(default=True)
    is_published = models.BooleanField(default=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    address = models.ForeignKey(to=Address, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Адрес')


    class Meta:
        ordering = ['-time_create']
        db_table = 'goods'
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(translit_to_eng(self.name))
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('goods:ad', kwargs={'ad_slug': self.slug})