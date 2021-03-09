from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from account.models import Profile


class Ad(models.Model):
    title = models.CharField("Название", max_length=200)
    type = models.ForeignKey('TypeAd', on_delete=models.CASCADE, verbose_name="Тип")
    created = models.DateTimeField("Создано", auto_now_add=True)
    beginning = models.DateTimeField("Опубликовать", default=timezone.now)
    ending = models.DateTimeField("Снять с публикации", blank=True, null=True)
    text = models.TextField("Текст", max_length=2000)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='profile', blank=True, null=True,
                             verbose_name="Пользователь")

    class Meta:
        ordering = ['-created']
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return self.title


class TypeAd(models.Model):
    title = models.CharField("Название", max_length=200, unique=True)

    class Meta:
        verbose_name = 'Тип объявления'
        verbose_name_plural = 'Типы объявлений'

    def __str__(self):
        return self.title
