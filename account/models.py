from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField("Дата рождения", blank=True, null=True)
    photo = models.ImageField("Аватарка", upload_to='users/%Y/%m/%d/', blank=True)
    status = models.ForeignKey('Status', on_delete=models.CASCADE, blank=True, null=True)
    phone = models.IntegerField("Телефон", blank=True, null=True)

    city = models.CharField("Город", default="Санкт-Петербург", max_length=100)
    street = models.CharField("Улица", max_length=100, default="Невский")
    house = models.PositiveSmallIntegerField("Дом", default=100)
    flat = models.PositiveSmallIntegerField("Квартира", blank=True, null=True)
    area = models.PositiveSmallIntegerField("Площадъ квартиры", blank=True, null=True)

    ban = models.BooleanField("Блокировка", default=False)
    ban_start = models.DateField("Начало блокировки", blank=True, null=True)
    ban_end = models.DateField("Конец блокировки", blank=True, null=True)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return self.user.username


class Status(models.Model):
    title = models.CharField("Название", max_length=200)

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

    def __str__(self):
        return self.title
