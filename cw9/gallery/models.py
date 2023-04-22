from django.contrib.auth import get_user_model
from django.db import models


class Photo(models.Model):
    image = models.ImageField(verbose_name='Фото', null=False, blank=True, upload_to='photos')
    description = models.CharField(verbose_name='Подпись', null=False, blank=False, max_length=200)
    author = models.ForeignKey(verbose_name='Автор', to=get_user_model(), related_name='photos', null=False, blank=False,
                               on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name='Дата и время создания', auto_now_add=True)

    def __str__(self):
        return f'{self.author}'