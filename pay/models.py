from django.contrib.auth.models import User
from django.db import models

from meter.models import Indication


class Accrued(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    accrued = models.SmallIntegerField("Начислено")
    payment = models.BooleanField("Оплата", default=False)
    created = models.DateField("Дата создания", auto_now_add=True)

    class Meta:
        ordering = ['-created']
        verbose_name = "Начисление"
        verbose_name_plural = "Начисления"

    def __str__(self):
        return self.user.username


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sum = models.SmallIntegerField("Оплачено")
    created = models.DateField("Дата создания", auto_now_add=True)

    class Meta:
        ordering = ['-created']
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"

    def __str__(self):
        return self.user.username
