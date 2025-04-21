from django.contrib.auth import get_user_model
from django.db import models

from goods.models import Goods

class Favorites(models.Model):

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='Пользователь')
    product = models.ForeignKey(to=Goods, on_delete=models.CASCADE, verbose_name='Товар')

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'

    def __str__(self):
        return f'Избранное пользователь {self.user} | товар {self.product.name}'

