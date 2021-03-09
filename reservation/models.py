from django.contrib.auth.models import User
from django.db import models

from account.models import Profile


class Reservation(models.Model):
    type = models.ForeignKey('TypeReservation', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    data_begin = models.DateTimeField()
    data_end = models.DateTimeField()
    executed = models.BooleanField(default=False)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-data_begin']
        verbose_name = 'Бронь'
        verbose_name_plural = 'Брони'

    def __str__(self):
        return self.type.title


class TypeReservation(models.Model):
    title = models.CharField(max_length=200, unique=True)

    class Meta:
        verbose_name = 'Тип брони'
        verbose_name_plural = 'Типы броний'

    def __str__(self):
        return self.title

